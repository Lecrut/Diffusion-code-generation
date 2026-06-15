import string
def split_and_clean(text):
    words = text.split()
    cleaned_words = []
    for word in words:
        stripped_word = word.strip(string.punctuation)
        if stripped_word:
            cleaned_words.append(stripped_word)
    return cleaned_words
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test... how are you?"
    result = split_and_clean(sample_string)
    print(result)