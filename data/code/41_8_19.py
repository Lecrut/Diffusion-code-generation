def format_string(input_str: str) -> str:
    """
    Creates a formatted string containing three versions of the input:
    1. The original string.
    2. All-caps version (using built-in method).
    3. Sentence-case version (created via slicing and manual logic, 
       as no standard sentence-case builtin exists in Python's str class directly).

    Args:
        input_str (str): The input string to process.

    Returns:
        str: A comma-separated string of original, all-caps, and sentence-case versions.
    """
    # Using built-in method for all caps
    upper_case = input_str.upper()

    # Logic for Sentence Case using slicing
    if len(input_str) == 0:
        lower_input = ""
    else:
        first_char = input_str[0].lower()
        rest_of_string = input_str[1:]
        
        # Convert the rest to lowercase and join (slicing used on split or just iterating chars, 
        # but slicing is required per prompt. We can slice by character index logic)
        sentence_case = first_char + "".join([c.lower() if c.isupper() else c for c in rest_of_string])

    return f"{input_str}, {upper_case}, {sentence_case}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "A"
    ]

    for test_string in samples:
        result = format_string(test_string)
        print(f"Input: '{test_string}'")
        print(result)
        print()  # Empty line between outputs for readability in console run