def extract_even_index_chars(phrase):
    result = []
    for index, char in enumerate(phrase):
        if index % 2 == 0:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_phrase = "Python Programming"
    even_index_chars = extract_even_index_chars(sample_phrase)
    print(even_index_chars)