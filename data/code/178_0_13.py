def split_string(s):
    return [word for word in s.strip().split() if word]

if __name__ == '__main__':
    sample = "   Hello,  world! This is a test.  "
    print(split_string(sample))