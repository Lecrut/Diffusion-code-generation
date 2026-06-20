from typing import Optional

def trim_whitespace(text: Optional[str]) -> str:
    if text is None:
        return ""
    return text.strip()

if __name__ == "__main__":
    sample_input = "   Hello World   "
    result = trim_whitespace(sample_input)
    print(result)
    print(repr(result))