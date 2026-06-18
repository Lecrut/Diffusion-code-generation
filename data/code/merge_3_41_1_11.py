def manipulate_case(input_string):
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions 
    of the input string using optimized built-in methods that operate in-place logic 
    internally (C-level optimizations).
    
    Args:
        input_string (str): The string to process.
        
    Returns:
        dict: A dictionary with keys 'lowercase', 'uppercase', and 'title'.
    """
    return {
        "lowercase": input_string.lower(),
        "uppercase": input_string.upper(),
        "title": input_string.title()
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    test_strings = [
        "hello world",
        "Python Programming 2024!",
        "---UNDEFINED---"
    ]

    results = {}

    for s in test_strings:
        res = manipulate_case(s)
        results[s] = {k: v.capitalize() if isinstance(v, str) else v 
                      for k, v in res.items()} # Just a cosmetic addition to the result dict for clarity on title case logic from other functions.

    print("Input String -> Output Dictionary")
    for input_str, output_dict in results.items():
        print(f"Input: '{input_str}'")
        print(output_dict)
        print("-" * 20)