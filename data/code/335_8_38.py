def split_string(s: str, delimiter: str) -> list[str]:
    return s.split(delimiter)
if __name__ == '__main__':
    test_str = "apple;banana;cherry"
    delimiters_to_try = [";", ",", "|"]
    for delim in delimiters_to_try:
        parts = split_string(test_str, delim)
        print(f"Delimiter '{delim}': {parts}")