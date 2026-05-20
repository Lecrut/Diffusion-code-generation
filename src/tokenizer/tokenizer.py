import re
from typing import Iterable
from transformers import AutoTokenizer

class CodeTokenizer:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-Coder-7B") -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._ensure_special_tokens()

    def _ensure_special_tokens(self) -> None:
        added = {}
        if self.tokenizer.pad_token_id is None:
            if self.tokenizer.eos_token is not None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            else:
                added["pad_token"] = "[PAD]"

        if self.tokenizer.mask_token_id is None:
            added["mask_token"] = "[MASK]"

        if added:
            self.tokenizer.add_special_tokens(added)

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
        return self.tokenizer.encode(
            text,
            add_special_tokens=add_special_tokens,
        )

    def encode(self, text: str, *, add_special_tokens: bool = True) -> list[int]:
        return self.encode_instruction(text, add_special_tokens=add_special_tokens)

    def decode(self, token_ids: Iterable[int], *, skip_special_tokens: bool = True) -> str:
        return self.tokenizer.decode(
            list(token_ids),
            skip_special_tokens=skip_special_tokens,
        )
