import string

def count_punctuation(text):
    punctuation_count = {char: text.count(char) for char in string.punctuation}
    return punctuation_count

if __name__ == '__main__':
    sample_text = "Hello, world! How are you? I'm fine."
    print(count_punctuation(sample_text))