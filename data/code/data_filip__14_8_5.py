def has_distinct_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_string = "abcde"
    result = has_distinct_characters(sample_string)
    print(result)