from typing import List

def string_to_chars(s: str) -> List[str]:
    return list(s)

if __name__ == '__main__':
    sample_string = "hello"
    result = string_to_chars(sample_string)
    print(result)