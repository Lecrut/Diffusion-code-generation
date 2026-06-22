def extract_distinct_words(text):
    punctuation = {',': '', '.': '', '!': '', '?': ''}
    cleaned_text = ''.join(punctuation.get(char, char) for char in text)
    words = cleaned_text.split()
    distinct_words = sorted(set(words), key=str.lower)
    return distinct_words

if __name__ == '__main__':
    sample_text = "Hello world! This is a test sentence, how are you doing today?"
    word_list = extract_distinct_words(sample_text)
    print(word_list)