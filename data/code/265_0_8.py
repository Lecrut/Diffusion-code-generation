def extract_even_index_chars(phrase):
    return ''.join(phrase[i] for i in range(len(phrase)) if i % 2 == 0)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_even_index_chars(sample_phrase))