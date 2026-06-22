def print_unicode_code_points(text):
    for char in text:
        print(ord(char))

if __name__ == '__main__':
    print_unicode_code_points("Hello, World!")