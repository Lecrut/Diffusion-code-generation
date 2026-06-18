from typing import Generator
def extract_first_letters(text: str) -> Generator[str, None, None]:
    return [word[0] for word in text.split() if len(word) > 1]
if __name__ == '__main__':
    sample_text = "Hello World Python Programming"
    result = "".join(extract_first_letters(sample_text))
    print(result)