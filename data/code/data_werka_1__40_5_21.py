import string

def word_to_first_letter(s):
    result = {}
    words = s.split()
    for word in words:
        cleaned_word = word.strip(string.punctuation)
        if cleaned_word:
            first_letter = cleaned_word[0]
            result[word] = first_letter
    return result
if __name__ == '__main__':
    sample_string = 'Hello, world! This is a test.'
    print(word_to_first_letter(sample_string))