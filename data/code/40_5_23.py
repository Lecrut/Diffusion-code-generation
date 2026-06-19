import string

def first_letter_of_words(text):
    words = text.split()
    result = {}
    for word in words:
        cleaned_word = word.strip(string.punctuation)
        if cleaned_word:
            result[cleaned_word] = cleaned_word[0]
    return result
if __name__ == '__main__':
    sample_text = 'Hello, world! This is a test.'
    print(first_letter_of_words(sample_text))