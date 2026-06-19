def reverse_string(s):
    return ''.join(chr(c) for c in range(len(s)-1, -1, -1))

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reversed_string = reverse_string(sample_string)
    print(reversed_string)