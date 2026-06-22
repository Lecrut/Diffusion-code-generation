def trim_string(s):
    return s.strip()

if __name__ == '__main__':
    sample = "   \t\n hello world \t\n   "
    result = trim_string(sample)
    print(result)