import string
def process_words(word_list):
    word_counts = {}
    for word in word_list:
        cleaned_word = word.lower()
        cleaned_word = cleaned_word.translate(str.maketrans('', '', string.punctuation))
        if cleaned_word:
            if cleaned_word in word_counts:
                word_counts[cleaned_word] += 1
            else:
                word_counts[cleaned_word] = 1
    return word_counts
if __name__ == '__main__':
    sample_words = [
        "Hello, world!",
        "Hello world.",
        "World!",
        "hello",
        "world",
        "Hello, world!"
    ]
    result = process_words(sample_words)
    print(result)