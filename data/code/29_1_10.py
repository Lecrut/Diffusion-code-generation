def reverse_word(text: str) -> str:
    """
    Returns a new string with the characters of the input reversed.
    
    This is considered Pythonic as it leverages slicing, which creates 
    a copy and reverses in C at high speed (O(n)).
    
    Args:
        text (str): The input string to reverse.
        
    Returns:
        str: A new string containing characters of the input in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    sample_1 = "Hello"
    result_1 = reverse_word(sample_1)
    
    sample_2 = "Pythonic Code!"
    result_2 = reverse_word(sample_2)
    
    print(f"'{sample_1}' reversed is: '{result_1}'")
    print(f"'{sample_2}' reversed is: '{result_2}'")