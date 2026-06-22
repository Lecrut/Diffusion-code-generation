from typing import Any

def trim_whitespace(text: Any) -> str:
    if not isinstance(text, str):
        text = str(text)
    return text.strip()

if __name__ == '__main__':
    sample_input = "   hello world   "
    result = trim_whitespace(sample_input)
    print(result)