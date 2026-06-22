def find_words_with_substring(text, substring):
    words = text.split()
    filtered_words = []
    for word in words:
        if substring in word:
            filtered_words.append(word)
    return filtered_words

if __name__ == '__main__':
    sample_text = "In computer science and linguistics, a token is the smallest element of a string that has semantic meaning."
    sample_substring = 'token'
    result = find_words_with_substring(sample_text, sample_substring)
    print(result)