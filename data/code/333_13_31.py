from typing import Generator
def first_letters(text: str) -> Generator[str, None, None]:
    return [word[0] for word in text.split() if len(word) > 1]
if __name__ == '__main__':
    sample = "Python Programming is Fun"
    result = "".join(first_letters(sample))
    print(result)