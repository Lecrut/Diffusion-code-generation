from typing import List

class StringTransformer:
    SEPARATOR: str = '_'
    CHAR_TO_REPLACE: str = ' '

    @staticmethod
    def split_text(text: str) -> List[str]:
        return text.split(StringTransformer.CHAR_TO_REPLACE)

    @staticmethod
    def join_text(parts: List[str]) -> str:
        return StringTransformer.SEPARATOR.join(parts)

    def transform(self, text: str) -> str:
        parts = StringTransformer.split_text(text)
        return StringTransformer.join_text(parts)

if __name__ == '__main__':
    text = "deterministic code generation task"
    transformer = StringTransformer()
    result = transformer.transform(text)
    print(result)