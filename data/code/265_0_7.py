def extract_even_index_chars(phrase):
    even_index_chars = []
    for index, char in enumerate(phrase):
        if index % 2 == 0:
            even_index_chars.append(char)
    return ''.join(even_index_chars)

if __name__ == '__main__':
    sample_phrase = "Programming is fun!"
    extracted_chars = extract_even_index_chars(sample_phrase)
    print(extracted_chars)