def string_transformations(s):
    return s, s.lower(), ''.join(c.swapcase() for c in s)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = string_transformations(sample_string)
    print(result)