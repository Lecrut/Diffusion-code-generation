def is_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    sample = "abcdefg"
    print(is_unique(sample))