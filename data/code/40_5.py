import string
def get_first_letters(text):
    result = {}
    words = text.split()
    for word in words:
        cleaned_word = ''.join(filter(str.isalpha, word))
        if cleaned_word:
            result[cleaned_word] = cleaned_word[0]
    return result
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    output_dict = get_first_letters(sample_string)
    print(output_dict)