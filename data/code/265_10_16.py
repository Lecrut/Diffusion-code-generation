def unique_chars_sorted(phrase):
    return ''.join(sorted(set(filter(str.isalpha, phrase))))

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_chars_sorted(sample_phrase))