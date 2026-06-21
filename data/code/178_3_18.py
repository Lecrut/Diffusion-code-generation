def extract_words(phrase):
    return [word for word in phrase.split(',') if word.strip()]

if __name__ == '__main__':
    sample_phrase = "apple,banana,,orange,"
    print(extract_words(sample_phrase))