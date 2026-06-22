def extract_even_index_chars(phrase):
    even_index_chars = [char for index, char in enumerate(phrase) if index % 2 == 0]
    return ''.join(even_index_chars)

if __name__ == '__main__':
    sample_phrase = "Python Programming"
    extracted_chars = extract_even_index_chars(sample_phrase)
    print(extracted_chars)