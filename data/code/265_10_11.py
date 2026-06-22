def unique_chars_sorted(phrase):
    char_set = set(phrase)
    sorted_chars = ''.join(sorted(char_set))
    return sorted_chars

if __name__ == '__main__':
    sample_phrase = "hello world"
    result = unique_chars_sorted(sample_phrase)
    print(result)