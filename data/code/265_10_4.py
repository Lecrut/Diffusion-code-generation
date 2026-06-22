def unique_sorted_chars(phrase):
    return ''.join(sorted(set(phrase)))

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_sorted_chars(sample_phrase))