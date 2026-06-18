def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the length of a given string (phrase).
    
    This function is optimized by directly returning len(), which 
    uses C-level implementation in Python, making it highly efficient.
    
    Args:
        phrase (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "a" * 1000,
        None  # This will raise a TypeError as expected per Python best practices
    ]

    print("Testing calculate_phrase_length function:\n")

    for i, sample in enumerate(samples):
        try:
            result = calculate_phrase_length(sample)
            status = "Success" if isinstance(result, int) else f"Unexpected return type: {type(result)}"
            print(f"Sample {i + 1}: '{sample[:20]}...' -> Length: {result} [{status}]")
        except Exception as e:
            # Expected behavior for invalid input like None
            status = "Handled Error (as expected)" if sample is not None else f"Expected Error ({e.__class__.__name__})"
            print(f"Sample {i + 1}: Input '{sample}' -> Error: {status}")