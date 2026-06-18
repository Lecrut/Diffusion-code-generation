import time

def reverse_string_recursive(s: str) -> str:
    """
    Recursively reverses a string without using slicing.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    if len(s) <= 1:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_direct(s: str) -> str:
    """Directly reverses a string using Python's slicing."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_cases = [
        "hello",
        "",
        "a",
        "Python is awesome!",
        "Recursion is powerful"
    ]

    print("Comparing Recursive vs Direct String Reversal Performance")
    print("-" * 50)

    for text in test_cases:
        start_time = time.perf_counter()
        result_recursive = reverse_string_recursive(text)
        end_time_recursive = time.perf_counter()

        start_time_direct = time.perf_counter()
        result_direct = reverse_string_direct(text)
        end_time_direct = time.perf_counter()

        # Verify correctness first (should always be equal for valid inputs)
        assert result_recursive == result_direct, "Mismatch between recursive and direct methods!"

        print(f"Input: '{text}'")
        print(f"Output: {result_recursive}")
        
        elapsed_rec = end_time_recursive - start_time_recursive
        elapsed_dir = end_time_direct - start_time_direct
        
        # Time complexity analysis note:
        # Recursive solution (T(n) = T(n-1) + O(1)): 
        #   Each call processes one character, leading to a linear time complexity of O(n).
        # Direct slicing method uses C-level optimization and is also effectively O(n),
        # but with significantly lower constant factors due to interpreter overhead avoidance.

        print(f"Recursive Time: {elapsed_rec:.8f} seconds")
        print(f"Direct Time:    {elapsed_dir:.8f} seconds")
        print("-" * 50)