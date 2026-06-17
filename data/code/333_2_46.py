import sys
def get_first_letters(sentence: str) -> list[str]:
    words = sentence.split()
    return [word[0].lower() for word in words if word]
if __name__ == '__main__':
    input_sentence = "Hello World Python Programming"
    result = get_first_letters(input_sentence)
    print("".join(result))