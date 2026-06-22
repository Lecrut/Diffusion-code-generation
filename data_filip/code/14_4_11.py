def has_duplicate_chars(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    sample_string = "programming"
    result = has_duplicate_chars(sample_string)
    print(result)