def has_duplicate_characters(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    sample = "hello"
    result = has_duplicate_characters(sample)
    print(result)