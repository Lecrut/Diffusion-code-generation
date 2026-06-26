import os
import re
from typing import Iterable, Sequence
from transformers import AutoTokenizer

CODE_EOS_TOKEN = "[CODE_EOS]"


class CodeTokenizer:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-Coder-7B") -> None:
        self.model_name = model_name
        tokenizer_path = os.getenv("TOKENIZER_MODEL_PATH", model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        self._code_eos_token_id: int | None = None
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

        added_vocab = getattr(self.tokenizer, "get_added_vocab", lambda: {})() or {}
        if CODE_EOS_TOKEN not in added_vocab:
            self.tokenizer.add_special_tokens({"additional_special_tokens": [CODE_EOS_TOKEN]})

        token_id = self.tokenizer.convert_tokens_to_ids(CODE_EOS_TOKEN)
        if token_id is None or token_id == self.tokenizer.unk_token_id:
            raise ValueError(f"{CODE_EOS_TOKEN} is not registered in the tokenizer.")
        self._code_eos_token_id = int(token_id)

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

    @property
    def code_eos_token_id(self) -> int:
        if self._code_eos_token_id is None:
            token_id = self.tokenizer.convert_tokens_to_ids(CODE_EOS_TOKEN)
            if token_id is None or token_id == self.tokenizer.unk_token_id:
                raise ValueError(f"{CODE_EOS_TOKEN} is not registered in the tokenizer.")
            self._code_eos_token_id = int(token_id)
        return self._code_eos_token_id

    @property
    def bos_token_id(self) -> int | None:
        return None if self.tokenizer.bos_token_id is None else int(self.tokenizer.bos_token_id)

    @property
    def special_token_ids(self) -> tuple[int, ...]:
        token_ids = set(int(token_id) for token_id in self.tokenizer.all_special_ids)
        token_ids.add(self.code_eos_token_id)
        token_ids.add(self.pad_token_id)
        token_ids.add(self.mask_token_id)
        if self.eos_token_id is not None:
            token_ids.add(self.eos_token_id)
        if self.bos_token_id is not None:
            token_ids.add(self.bos_token_id)
        return tuple(sorted(token_ids))

    @property
    def corruption_protected_token_ids(self) -> tuple[int, ...]:
        """Special tokens that should never be replaced by [MASK] during training."""
        return tuple(token_id for token_id in self.special_token_ids if token_id != self.code_eos_token_id)

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
        if add_special_tokens:
            token_ids.append(self.code_eos_token_id)
        return token_ids

    def batch_encode_instruction(
        self,
        texts: Sequence[str],
        *,
        add_special_tokens: bool = True,
        max_length: int | None = None,
    ) -> list[list[int]]:
        normalized_texts = [self.normalize_instruction(text) for text in texts]
        encoded = self.tokenizer(
            normalized_texts,
            add_special_tokens=add_special_tokens,
            truncation=max_length is not None,
            max_length=max_length,
            padding=False,
        )
        return [list(ids) for ids in encoded["input_ids"]]

    def batch_encode_code(
        self,
        texts: Sequence[str],
        *,
        add_special_tokens: bool = True,
        max_length: int | None = None,
    ) -> list[list[int]]:
        tokenizer_max_length = max_length
        if add_special_tokens and max_length is not None:
            tokenizer_max_length = max(max_length - 1, 0)
        encoded = self.tokenizer(
            list(texts),
            add_special_tokens=add_special_tokens,
            truncation=tokenizer_max_length is not None,
            max_length=tokenizer_max_length,
            padding=False,
        )
        code_ids = [list(ids) for ids in encoded["input_ids"]]
        if add_special_tokens:
            for ids in code_ids:
                ids.append(self.code_eos_token_id)
        return code_ids

    def encode(self, text: str, *, add_special_tokens: bool = True) -> list[int]:
        return self.encode_instruction(text, add_special_tokens=add_special_tokens)

    def decode(self, token_ids: Iterable[int], *, skip_special_tokens: bool = True) -> str:
        return self.tokenizer.decode(
            list(token_ids),
            skip_special_tokens=skip_special_tokens,
        )
