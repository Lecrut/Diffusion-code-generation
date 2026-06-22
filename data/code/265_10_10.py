def extract_unique_chars(phrase):
    unique_chars = set(phrase)
    return ''.join(sorted(unique_chars))

if __name__ == '__main__':
    sample_phrase = "Programming is fun!"
    result = extract_unique_chars(sample_phrase)
    print(result)