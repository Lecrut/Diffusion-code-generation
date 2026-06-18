def reverse_sentence(sentence: str) -> str:
    """
    Reverses a given sentence efficiently by slicing, 
    which is an O(n) operation in Python.
    
    Args:
        sentence (str): The input string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for test_input in samples:
        reversed_output = reverse_sentence(test_input)
        print(f"Original:  {test_input}")
        print(f"Reversed:  {reversed_output}\n")