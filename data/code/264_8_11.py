def find_words_with_substring(text, substring):
    words = text.split()
    filtered_words = [word for word in words if substring in word]
    return filtered_words

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog."
    sample_substring = 'o'
    result = find_words_with_substring(sample_text, sample_substring)
    print(result)