def has_distinct_characters(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string = "abcdef"
    result = has_distinct_characters(test_string)
    print(result)