def trim_string(s):
    return s.strip()

if __name__ == '__main__':
    sample = "   hello   world   "
    result = trim_string(sample)
    print(result)