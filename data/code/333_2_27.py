import sys
def get_first_letters(sentence):
    words = sentence.split()
    if not words:
        return ""
    first_chars = [word[0] for word in words]
    return "".join(first_chars)
if __name__ == '__main__':
    sample_sentence = "Hello World Python Programming"
    result = get_first_letters(sample_sentence)
    print(result)