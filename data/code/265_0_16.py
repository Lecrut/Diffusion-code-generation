def is_even_index(index):
    return index % 2 == 0

def extract_even_index_chars(phrase):
    result = ""
    for index, char in enumerate(phrase):
        if is_even_index(index):
            result += char
    return result

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    even_index_chars = extract_even_index_chars(sample_phrase)
    print(even_index_chars)