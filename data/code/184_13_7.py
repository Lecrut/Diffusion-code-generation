def substring_exists(text, substring):
    return text.find(substring) != -1

if __name__ == '__main__':
    sample_text = "This is a large corpus of text."
    sample_substring = "corpus"
    print(substring_exists(sample_text, sample_substring))