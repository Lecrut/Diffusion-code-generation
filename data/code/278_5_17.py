def print_ascii_values(characters):
    ascii_dict = {char: ord(char) for char in characters}
    for char, ascii_val in ascii_dict.items():
        print(f"{char}: {ascii_val}")

if __name__ == '__main__':
    sample_chars = "abc"
    print("Printing ASCII values:")
    print_ascii_values(sample_chars)