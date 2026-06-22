def extract_unique_chars(phrase):
    unique_chars = set(phrase)
    sorted_chars = ''.join(sorted(unique_chars))
    return sorted_chars

if __name__ == '__main__':
    sample_phrase = "Python programming is fun!"
    result = extract_unique_chars(sample_phrase)
    print(result)