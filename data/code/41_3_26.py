def process_string(s):
    return (s, s.lower(), ''.join(c.swapcase() for c in s))

if __name__ == '__main__':
    sample_string = "Hello World"
    result = process_string(sample_string)
    print(result)