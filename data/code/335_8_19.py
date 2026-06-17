def split_string(s: str, delimiter: str) -> list[str]:
    return s.split(delimiter)
if __name__ == '__main__':
    test_str = "apple;banana;cherry"
    delimiters = [";", ",", ":"]
    for delim in delimiters:
        parts = split_string(test_str, delim)
        print(f"Delimiter '{delim}': {parts}")