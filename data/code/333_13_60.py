from typing import Generator
def extract_first_letters(text: str) -> Generator[str, None, None]:
    return [word[0] for word in text.split() if word]
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = ''.join(extract_first_letters(sample_input))
    print(result)