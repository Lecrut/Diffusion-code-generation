def reverse_word(s: str) -> str:
    """
    Returns a single string as input, returns its reversed version.
    
    The implementation uses slicing which is efficient in Python 
    and creates a new string with characters in reverse order.
    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(n) for creating the reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "hello",
        "Python programming",
        "",
        "a",
        "racecar"
    ]
    
    for test_input in samples:
        result = reverse_word(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')