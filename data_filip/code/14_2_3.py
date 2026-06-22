def has_unique_chars(s: str) -> bool:
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "python"
    result = has_unique_chars(test_string)
    print(result)