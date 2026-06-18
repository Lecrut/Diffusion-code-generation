def combine_strings(str1: str, str2: str) -> str:
    """Combines two strings separated by a single space."""
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input or command-line arguments
    string_a = "hello"
    string_b = "world"

    result_string = combine_strings(string_a, string_b)

    print(result_string)