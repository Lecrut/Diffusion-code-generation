def reverse_string(s):
    return ''.join(reversed(list(s))) if s else ""

if __name__ == '__main__':
    sample = "Hello"
    print(reverse_string(sample))