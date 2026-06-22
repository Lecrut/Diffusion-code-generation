from typing import Union

def trim_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_text = "   Hello World   "
    result = trim_whitespace(sample_text)
    print(result)