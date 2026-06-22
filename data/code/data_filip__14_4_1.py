def has_duplicates(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    sample = "hello"
    print(has_duplicates(sample))