def reverse_string(s):
    return ''.join(reversed(str(s))) if s is None else str(s)[::-1]

if __name__ == '__main__':
    print(reverse_string("Hello, World!"))