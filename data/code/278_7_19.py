def print_unicode_code_points(s):
    for char in s:
        print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    print_unicode_code_points("Hello, World!")