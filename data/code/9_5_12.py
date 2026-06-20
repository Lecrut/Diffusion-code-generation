def trim_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    sample = "   \t\n hello world \t\n   "
    print(trim_whitespace(sample))