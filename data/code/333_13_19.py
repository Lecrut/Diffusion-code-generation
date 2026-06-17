from typing import List
def extract_first_letters(text: str) -> List[str]:
    return [word[0] for word in text.split() if len(word) > 0]
if __name__ == '__main__':
    sample = "Hello world Python programming"
    result = extract_first_letters(sample)
    print("".join(result))