import sys
def get_first_letter_of_each_word(sentence: str) -> list[str]:
    return [word[0].lower() for word in sentence.split()]
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = get_first_letter_of_each_word(sample_input)
    print("".join(result))