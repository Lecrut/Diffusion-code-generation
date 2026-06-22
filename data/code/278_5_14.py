def print_char_ascii(char_set):
    if not all(isinstance(c, str) and len(c) == 1 for c in char_set):
        raise ValueError("Input must be a set of single characters")
    
    for char in char_set:
        ascii_val = ord(char)
        print(f"Character: {char}, ASCII Value: {ascii_val}")

if __name__ == '__main__':
    sample_chars = {'a', 'b', 'c', 'd'}
    print("Printing each character with its ASCII value:")
    print_char_ascii(sample_chars)