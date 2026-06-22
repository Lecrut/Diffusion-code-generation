import re

_special_char_pattern = re.compile(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?~`]')

def contains_special_characters(text: str) -> bool:
    if not text:
        return False
    return bool(_special_char_pattern.search(text))

if __name__ == '__main__':
    test_cases = ["hello world", "hello! world", "no_special_here", "has @ symbol"]
    for tc in test_cases:
        result = contains_special_characters(tc)
        print(result)