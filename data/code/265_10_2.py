def unique_chars_sorted(phrase):
    return ''.join(sorted(set(phrase)))

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_chars_sorted(sample_phrase))