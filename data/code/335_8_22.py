def split_string(s: str, delimiter: str) -> list[str]:
    return s.split(delimiter)
if __name__ == '__main__':
    test_string = "apple;banana;cherry"
    separator = ";"
    result = split_string(test_string, separator)
    print(result)