from typing import Generator
def extract_first_letters(text: str) -> Generator[str, None, None]:
    return [word[0] for word in text.split() if len(word) > 0]
if __name__ == '__main__':
    sample_text = "Python is great and fun"
    result = list(extract_first_letters(sample_text))
    print("".join(result), end="")