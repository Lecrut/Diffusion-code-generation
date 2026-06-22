def print_char_ascii(char_set):
    for char in char_set:
        ascii_value = ord(char)
        print(f"{char}: {ascii_value}")

if __name__ == '__main__':
    sample_chars = {'a', 'b', 'c'}
    print("Printing characters and their ASCII values:")
    print_char_ascii(sample_chars)