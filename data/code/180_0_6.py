import sys
def check_word_presence(text, word):
    return word in text.lower()
if __name__ == '__main__':
    sample_string = "The quick Brown fox jumps over the lazy dog."
    sample_word = "brown"
    result = check_word_presence(sample_string, sample_word)
    print(result)