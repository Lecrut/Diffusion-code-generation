def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string using built-in methods.
    
    Args:
        text (str): The input string potentially containing spaces and other whitespace.
        
    Returns:
        str: A new string with no whitespace characters.
    """
    return "".join(text.split())

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "Hello World",
        "  Leading and trailing spaces   ",
        "\tTab\nNewline\rCarriage return",
        "",
        "No-spaces-here"
    ]

    for sample in samples:
        result = remove_all_spaces(sample)
        print(f'Input: {repr(sample)}')
        print(f'Result: {result}\n')