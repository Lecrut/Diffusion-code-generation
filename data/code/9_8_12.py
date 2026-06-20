def trim_edge_spaces(input_str: str) -> str:
    return input_str.strip()

if __name__ == '__main__':
    test_data = {
        "whitespace_front_back": "  Pythonic elegance  ",
        "tabs_and_newlines": "\t\ntrimmed\n\t",
        "empty_core": "   ",
        "no_whitespace": "compact"
    }
    for label, value in test_data.items():
        print(trim_edge_spaces(value))