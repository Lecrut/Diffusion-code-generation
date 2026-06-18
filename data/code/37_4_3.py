def combine_strings(str1: str, str2: str) -> None:
    """Prints the combination of two strings separated by a space."""
    result = f"{str1} {str2}"
    print(result)

if __name__ == "__main__":
    # Hard-coded sample values to avoid any interactive input or arguments.
    value_one = "Hello"
    value_two = "World"

    combine_strings(value_one, value_two)