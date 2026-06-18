import sys
def extract_first_letters(text: str) -> list[str]:
    return [word[0] for word in text.split() if len(word) > 1]
if __name__ == '__main__':
    sample_input = "Python Programming is Fun"
    result = extract_first_letters(sample_input)
    print("".join(result))