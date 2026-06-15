def process_string(text):
    words_with_case = []
    words_lowercase = []
    for word in text.split():
        words_with_case.append(word)
        words_lowercase.append(word.lower())
    return words_with_case, words_lowercase
if __name__ == '__main__':
    sample_string = "This Is A Sample String With Mixed Cases"
    words_cased, words_lowercased = process_string(sample_string)
    print("Words with original capitalization:", words_cased)
    print("Words in lowercase:", words_lowercased)