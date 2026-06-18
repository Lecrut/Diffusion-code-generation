import re

def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string using a regular expression.
    
    Args:
        text (str): The input string containing various types of whitespace.
        
    Returns:
        str: A new string with all whitespace characters removed.
    """
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user interaction or file I/O
    test_cases = [
        "  Hello World  ",
        "\t\nTest String\t\n",
        "NoSpacesHere12345!",
        "   Mixed\tWhitespace\ndata: spaces -> gone"
    ]

    results = []
    for input_str in test_cases:
        output_str = remove_all_spaces(input_str)
        results.append((input_str, output_str))

    # Print sample execution results to verify correctness
    print("Sample Execution Results:")
    for original_result in results:
        if len(original_result[1]) == 0:
            display_text = " (empty)"
        else:
            display_text = f" ({repr(original_result[1][:20]+'...')})"
        print(f"Input: {repr(original_result[0])} => Output{display_text}")