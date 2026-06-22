def extract_and_sort_characters(phrase):
    unique_chars = set(phrase)
    sorted_chars = ''.join(sorted(unique_chars))
    return sorted_chars

if __name__ == '__main__':
    sample_phrase = "Python is great!"
    result = extract_and_sort_characters(sample_phrase)
    print(result)