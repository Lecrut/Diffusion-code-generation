def print_ascii_values(characters):
    for char in characters:
        print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    print_ascii_values("abc")