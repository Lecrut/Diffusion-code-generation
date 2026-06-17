import sys
def get_first_letters(sentence):
    words = sentence.split()
    return [word[0] for word in words if len(word) > 0]
if __name__ == '__main__':
    sample_sentence = "Hello World Python Programming"
    result = get_first_letters(sample_sentence)
    print("".join(result))