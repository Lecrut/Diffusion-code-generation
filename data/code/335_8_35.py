def split_string(s: str, delimiter: str) -> list[str]:
    return s.split(delimiter)
if __name__ == '__main__':
    test_string = "apple;banana;cherry"
    delimiters_to_try = [";", ",", "|"]
    for delim in delimiters_to_try:
        result = split_string(test_string, delim)
        print(f"Delimiter '{delim}': {result}")