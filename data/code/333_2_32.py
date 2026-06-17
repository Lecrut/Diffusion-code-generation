import sys
def get_first_letter(sentence: str) -> list[str]:
    return [word[0].upper() for word in sentence.split(' ') if word]
if __name__ == '__main__':
    sample_sentence = "Hello World Python Programming"
    result = get_first_letter(sample_sentence)
    print("".join(result))
    sys.exit(0)