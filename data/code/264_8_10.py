def find_words_with_substring(text, substring):
    return [word for word in text.split() if substring in word]

if __name__ == '__main__':
    sample_text = "hello world this is a test string with the substring"
    sample_substring = "sub"
    print(find_words_with_substring(sample_text, sample_substring))