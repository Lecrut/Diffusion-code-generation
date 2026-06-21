def split_string(s):
    return [word for word in s.strip().split() if word]

if __name__ == '__main__':
    sample = "   This is  a test string with multiple spaces.   "
    print(split_string(sample))