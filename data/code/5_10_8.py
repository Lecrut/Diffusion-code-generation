import string
from typing import Iterable, List

_VALID_INPUT = (str, bytes)

def _is_valid_item(item: object) -> bool:
    if not isinstance(item, _VALID_INPUT):
        return False
    if isinstance(item, bytes):
        try:
            item.decode("utf-8")
        except (UnicodeDecodeError, AttributeError):
            return False
    return True

def _transform_item(item: str) -> str:
    if not item:
        return item
    result = []
    for char in item:
        if char.isspace():
            result.append(char)
        else:
            if not result or result[-1].isspace():
                result.append(char.upper())
            else:
                result.append(char.lower())
    return "".join(result)

def capitalize_words(words: Iterable[object]) -> List[str]:
    validated = []
    for item in words:
        if _is_valid_item(item):
            if isinstance(item, bytes):
                item = item.decode("utf-8")
            validated.append(item)
    
    result = []
    for word in validated:
        transformed = _transform_item(word)
        result.append(transformed)
    
    return result

if __name__ == '__main__':
    sample_data = [
        "hello world",
        "python programming",
        "  mixed   spacing  ",
        "UPPER CASE",
        "mIxEd CaSe WoRdS",
        b"bytes input here",
        123,
        None,
        "single"
    ]
    output = capitalize_words(sample_data)
    print(output)