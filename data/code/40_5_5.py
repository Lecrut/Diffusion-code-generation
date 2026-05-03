import string
def word_first_letters(text):
    word_dict = {}
    words = text.split()
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalpha())
        if cleaned_word:
            word_dict[word] = cleaned_word[0]
    return word_dict
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    result = word_first_letters(sample_string)
    print(result)