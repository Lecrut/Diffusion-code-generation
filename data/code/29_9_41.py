reverse_string = lambda s: ''.join(chr(c) for c in range(ord(s[-1]), ord(s[0]) - 1, -1)) if s else ''
if __name__ == '__main__':
    sample_string = "example"
    print(reverse_string(sample_string))