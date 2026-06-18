import string
def process_words(word_list):
    word_counts = {}
    for word in word_list:
        cleaned_word = word.lower()
        translator = str.maketrans('', '', string.punctuation)
        no_punct_word = cleaned_word.translate(translator)
        if no_punct_word:
            if no_punct_word in word_counts:
                word_counts[no_punct_word] += 1
            else:
                word_counts[no_punct_word] = 1
    return word_counts
if __name__ == '__main__':
    sample_words = [
        "Hello, world!",
        "World.",
        "hello",
        "hello world",
        "World!"
    ]
    result = process_words(sample_words)
    print(result)