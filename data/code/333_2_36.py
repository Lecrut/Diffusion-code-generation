import sys
def get_first_letters(sentence: str) -> list[str]:
    letters = []
    for word in sentence.split():
        if len(word) > 0:
            letters.append(word[0])
    return letters
if __name__ == '__main__':
    sample_sentence = "Hello World Python Programming"
    result_letters = get_first_letters(sample_sentence)
    output_string = "".join(result_letters)
    print(output_string, end='')