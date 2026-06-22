def has_duplicates(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    sample_string = "programming"
    result = has_duplicates(sample_string)
    print(result)