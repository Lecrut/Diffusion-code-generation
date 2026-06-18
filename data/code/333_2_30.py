import sys
def get_first_letters(sentence: str) -> list[str]:
    return [word[0] for word in sentence.split() if word]
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = get_first_letters(sample_input)
    print("".join(result))