import re
def split_and_clean(text):
    words = text.split()
    cleaned_words = []
    for word in words:
        cleaned_word = word.strip('.,!?;:"\'()[]{}')
        if cleaned_word:
            cleaned_words.append(cleaned_word)
    return cleaned_words
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    result = split_and_clean(sample_string)
    print(result)