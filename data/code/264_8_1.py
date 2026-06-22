def find_words_with_substring(text, substring):
    return [word for word in text.split() if substring in word]

if __name__ == '__main__':
    sample_text = "Hello world, this is a test string with the substring 'test'."
    sample_substring = 'test'
    print(find_words_with_substring(sample_text, sample_substring))