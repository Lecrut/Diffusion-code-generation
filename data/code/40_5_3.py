import string
def get_first_letters(text):
    result = {}
    words = text.split()
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalpha())
        if cleaned_word:
            result[word] = cleaned_word[0]
    return result
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test."
    sample_string2 = "Python is fun, isn't it?"
    sample_string3 = "  What's up?  End."
    print(get_first_letters(sample_string1))
    print(get_first_letters(sample_string2))
    print(get_first_letters(sample_string3))