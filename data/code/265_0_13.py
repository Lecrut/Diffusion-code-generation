EVEN_INDEX_CHARS = ''.join(chr(i) for i in range(0, 128, 2))

def extract_even_index_chars(phrase):
    return ''.join(char for index, char in enumerate(phrase) if index % 2 == 0)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    result = extract_even_index_chars(sample_phrase)
    print(result)