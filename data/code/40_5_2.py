import string
def word_first_letters(text):
    result = {}
    words = text.split()
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalpha())
        if cleaned_word:
            result[cleaned_word] = cleaned_word[0]
    return result
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    output_dict = word_first_letters(sample_string)
    print(output_dict)