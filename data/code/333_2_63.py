import sys
def get_first_letters(sentence: str) -> list[str]:
    return [word[0].lower() for word in sentence.split()]
if __name__ == '__main__':
    sample_sentence = "Hello World Python Programming"
    result = get_first_letters(sample_sentence)
    print("".join(result))