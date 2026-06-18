from typing import List
def extract_first_letters(text: str) -> List[str]:
    return [word[0].lower() for word in text.split() if len(word) > 1]
if __name__ == '__main__':
    sample = "Hello World Python Programming"
    result = extract_first_letters(sample)
    print("".join(result))