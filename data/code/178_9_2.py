def process_string(text):
    words = text.split()
    capitalized_words = []
    lowercase_words = []
    for word in words:
        capitalized_words.append(word)
        lowercase_words.append(word.lower())
    return capitalized_words, lowercase_words
if __name__ == '__main__':
    sample_string = "This Is A Sample String With Mixed Cases"
    capitalized, lowercase = process_string(sample_string)
    print("Capitalized Words:", capitalized)
    print("Lowercase Words:", lowercase)