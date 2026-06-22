def print_ascii_values(char_set):
    for char in char_set:
        print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    sample_chars = {'a', 'b', 'c'}
    print_ascii_values(sample_chars)