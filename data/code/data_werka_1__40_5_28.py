import string

def first_letter_of_words(text):
    words = text.split()
    result = {}
    for word in words:
        clean_word = word.strip(string.punctuation)
        if clean_word:
            result[clean_word] = clean_word[0]
    return result
if __name__ == '__main__':
    sample_text = 'Hello, world! This is a test.'
    print(first_letter_of_words(sample_text))