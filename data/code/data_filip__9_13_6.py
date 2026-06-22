from typing import Any

def trim_whitespace(value: Any) -> str:
    if not isinstance(value, str):
        return str(value).strip()
    return value.strip()

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = trim_whitespace(sample_input)
    print(result)