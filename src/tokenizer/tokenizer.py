import re
from pathlib import Path
from typing import Iterable
from transformers import AutoTokenizer

class CodeTokenizer:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-Coder-7B") -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(self._resolve_model_source(model_name))
        self._ensure_special_tokens()

    @staticmethod
    def _resolve_model_source(model_name: str) -> str:
        model_path = Path(model_name)
        if model_path.exists():
            return str(model_path)

        if "/" not in model_name:
            return model_name

        cache_root = Path.home() / ".cache" / "huggingface" / "hub"
        snapshots_dir = cache_root / f"models--{model_name.replace('/', '--')}" / "snapshots"
        if not snapshots_dir.exists():
            return model_name

        snapshots = [
            path
            for path in snapshots_dir.iterdir()
            if path.is_dir() and (path / "tokenizer.json").exists()
        ]
        if not snapshots:
            return model_name

        return str(max(snapshots, key=lambda path: path.stat().st_mtime))

    def _ensure_special_tokens(self) -> None:
        added = {}
        if (
            self.tokenizer.pad_token_id is None
            or self.tokenizer.pad_token_id == self.tokenizer.eos_token_id
        ):
            added["pad_token"] = "[PAD]"

        if self.tokenizer.mask_token_id is None:
            added["mask_token"] = "[MASK]"

        if added:
            self.tokenizer.add_special_tokens(added)

        if self.tokenizer.pad_token_id == self.tokenizer.eos_token_id:
            raise ValueError("pad_token_id and eos_token_id must be distinct for diffusion training.")

    @property
    def vocab_size(self) -> int:
        return int(len(self.tokenizer))

    @property
    def pad_token_id(self) -> int:
        return int(self.tokenizer.pad_token_id)

    @property
    def mask_token_id(self) -> int:
        return int(self.tokenizer.mask_token_id)

    @property
    def eos_token_id(self) -> int | None:
        return None if self.tokenizer.eos_token_id is None else int(self.tokenizer.eos_token_id)

    @staticmethod
    def normalize_instruction(text: str) -> str:
        normalized = text.lower().strip()
        normalized = re.sub(r"\s+", " ", normalized)
        return normalized

    def encode_instruction(self, text: str, *, add_special_tokens: bool = True) -> list[int]:
        normalized_text = self.normalize_instruction(text)
        return self.tokenizer.encode(
            normalized_text,
            add_special_tokens=add_special_tokens,
        )

    def encode_code(self, text: str, *, add_special_tokens: bool = True) -> list[int]:
        token_ids = self.tokenizer.encode(
            text,
            add_special_tokens=add_special_tokens,
        )
        if add_special_tokens and self.eos_token_id is not None:
            if not token_ids or token_ids[-1] != self.eos_token_id:
                token_ids.append(self.eos_token_id)
        return token_ids

    def encode(self, text: str, *, add_special_tokens: bool = True) -> list[int]:
        return self.encode_instruction(text, add_special_tokens=add_special_tokens)

    def decode(self, token_ids: Iterable[int], *, skip_special_tokens: bool = True) -> str:
        return self.tokenizer.decode(
            list(token_ids),
            skip_special_tokens=skip_special_tokens,
        )
