CHAR_SET = "abcdefghijklmnopqrstuvwxyz"

def print_chars_with_ascii(char_set):
    for char in char_set:
        ascii_val = ord(char)
        print(f"{char}: {ascii_val}")

if __name__ == '__main__':
    print_chars_with_ascii(CHAR_SET)