def print_chars_with_ascii(char_set):
    for char in char_set:
        print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    sample_chars = {'a', 'b', 'c'}
    print_chars_with_ascii(sample_chars)