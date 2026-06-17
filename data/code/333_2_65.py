import sys
def get_first_letters(sentence: str) -> list[str]:
    words = sentence.split()
    return [word[0] for word in words if word]
if __name__ == '__main__':
    sample_inputs = ["Hello World", "Python Programming"]
    for input_sentence in sample_inputs:
        result = get_first_letters(input_sentence)
        print("".join(result))