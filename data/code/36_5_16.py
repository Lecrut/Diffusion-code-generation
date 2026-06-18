import sys

def reverse_string_generator(s):
    """
    Generates characters of a string in reverse order as an iterator.
    
    This function optimizes memory usage by not creating a copy of the entire 
    reversed sequence at once. Instead, it accesses characters from index 0 to n-1 
    (where n is length) and yields them starting from the last character down to zero.
    
    Args:
        s (str): The input string to process. Can be very large; this function avoids slicing or reversing copies.
        
    Yields:
        str: Individual characters of the input string in reverse order.
    """
    n = len(s)
    if n == 0:
        return
    
    # Start from the last index and move backwards to 0
    for i in range(n - 1, -1, -1):
        yield s[i]

if __name__ == '__main__':
    sample_string = "Hello World"
    
    print("Reverse characters generator demonstration:")
    
    # Convert the generator to a list here just to show output clearly for this demo
    reversed_chars = [char for char in reverse_string_generator(sample_string)]
    result = "".join(reversed_chars)
    print(f"Input:  {sample_string}")
    print(f"Output: {result}")

    # Additional large string test case without external files or network access
    large_text = "A" * (10**6) + "B"
    
    reversed_large = [char for char in reverse_string_generator(large_text)]
    last_char_count = sum(1 for char in reversed_large if char == 'B')