import string

def manipulate_case(input_string: str) -> dict:
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of the input string.
    
    Args:
        input_string (str): The string to process.
        
    Returns:
        dict: A dictionary with keys 'lowercase', 'uppercase', and 'title_case'.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Using built-in methods which are implemented in C for maximum efficiency.
    lowercase = input_string.lower()
    uppercase = input_string.upper()
    
    # Title casing is efficient as it typically uses optimized internal logic 
    # to capitalize the first character of each word and lower-case subsequent characters.
    title_case = input_string.title()

    return {
        'lowercase': lowercase,
        'uppercase': uppercase,
        'title_case': title_case
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user interaction.
    samples = [
        "Hello World!",
        "Python Programming",
        "  spaced and mixed   ",
        ""
    ]

    for test_input in samples:
        result = manipulate_case(test_input)
        print(f"Input: \"{test_input}\"")
        print(result)
        print("-" * 30)