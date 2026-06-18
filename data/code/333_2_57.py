import sys
def get_first_letters(sentence: str) -> list[str]:
    words = [word.strip() for word in sentence.split()]
    return [word[0] if word else '' for word in words]
if __name__ == '__main__':
    sample_sentence: str = "Hello World Python Programming"
    result: list[str] = get_first_letters(sample_sentence)
    print(''.join(result))