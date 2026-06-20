def trim_string(s):
    return s.strip()

if __name__ == '__main__':
    sample = "   Hello, World!   "
    result = trim_string(sample)
    print(repr(result))