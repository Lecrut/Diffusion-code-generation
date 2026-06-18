def combine_strings(str1: str, str2: str) -> str:
    """Combines two input strings by concatenating them."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    string_a = "Hello"
    string_b = "World"

    result = combine_strings(string_a, string_b)
    print(result)