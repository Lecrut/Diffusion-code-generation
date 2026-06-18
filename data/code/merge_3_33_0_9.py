def remove_all_spaces(text: str) -> str:
    """Returns a new string with all whitespace characters removed."""
    return "".join(char for char in text if not char.isspace())

if __name__ == '__main__':
    sample_input = "Hello, World! This is   a  test."
    result = remove_all_spaces(sample_input)
    print(result)