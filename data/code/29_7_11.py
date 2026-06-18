import sys

def reverse_string_minimal_memory(s: str) -> str:
    """
    Reverses a string with minimal memory usage by converting it to a list,
    reversing in place, and joining back into a single new string object.
    
    This approach avoids creating multiple intermediate large strings 
    (like slicing s[::-1] which creates copies) or deep recursion,
    focusing on O(n) time complexity with limited extra space proportional 
    to the input size for character storage.
    
    Args:
        s (str): The input string to reverse
        
    Returns:
        str: A new string representing the reversed original string
        
    Note: While Python strings are immutable, this function minimizes memory 
    by using a list of characters which is mutable and compact before joining.
    """
    # Convert string to list for in-place modification simulation
    char_list = list(s)
    
    # Two-pointer approach to reverse the list in place (O(n/2) swaps, O(1) extra space beyond input conversion)
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap characters at pointers using tuple unpacking which is efficient
        char_list[left], char_list[right] = char_list[right], char_list[left]
        
        # Move pointers inward
        left += 1
        right -= 1
        
    # Join the modified list into a single string result. 
    # This creates one final large string object, which is unavoidable in Python 
    # without external libraries like numpy (which aren't standard).
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    samples = [
        "hello",
        "Python Programming",
        "",
        "a" * 100,
        "Race car"
    ]

    for test_input in samples:
        reversed_result = reverse_string_minimal_memory(test_input)
        print(f"Original: '{test_input}'")
        print(f"Reversed: {reversed_result}")
        print("-" * 30)