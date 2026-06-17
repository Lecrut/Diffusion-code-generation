import sys
def get_first_letters(sentence: str) -> list[str]:
    words = [word for word in sentence.split() if word]
    return [word[0].upper() for word in words]
if __name__ == '__main__':
    sample_sentence = "Hello World Python Programming"
    result = get_first_letters(sample_sentence)
    print("".join(result))