import sys
def get_first_letter(sentence):
    words = sentence.split()
    return ''.join(word[0] for word in words if word)
if __name__ == '__main__':
    sample_sentence = "Hello World Python Programming"
    result = get_first_letter(sample_sentence)
    print(result)