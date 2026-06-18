def split_string(s: str, delimiter: str) -> list[str]:
    return s.split(delimiter)
if __name__ == '__main__':
    test_input = "apple;banana;cherry"
    result = split_string(test_input, ";")
    print(result)