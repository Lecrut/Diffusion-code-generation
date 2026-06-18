import sys

def reverse_char_generator(string_data: str) -> None:
    """
    Generator function that yields characters of an input string in reverse order.
    
    Optimizes memory usage by not creating a copy or reversed list of the entire 
    string for large inputs; it simply iterates from the last index to 0 (or end).
    
    Args:
        string_data (str): The input string containing characters to yield.
        
    Yields:
        str: Single character strings from the input, in reverse order.
        
    Example usage:
        for ch in reverse_char_generator("abc"):
            print(ch) 
        Output: cba

"""
    
    length = len(string_data)
    
    if length == 0:
        return
    
    # Iterate backwards through string indices
    current_index = length - 1
    
    while current_index >= 0:
        yield string_data[current_index]
        
        current_index -= 1

if __name__ == '__main__':
    test_string_1 = "Hello, World!"
    
    # Print a separator for clarity before processing sample inputs
    print("--- Sample Input ---")
    print(f"Original String: '{test_string_1}'\nReverse Output:")
    print("-- Result --")

    try:
        # Generate and collect characters from the generator to demonstrate output
        results = []
        
        for char in reverse_char_generator(test_string_1):
            results.append(char)
            
        result_str = "".join(results)
        print(result_str)  # Output should be '!dlroW ,olleH'

    except Exception:
        pass
    
    test_string_large_size = "A" * (50 * 1e3 + 2048)  # Simulate very large string size (~50MB if char is not optimized, but still manageable in Python strings directly due to their nature. )

    print("--- Large String Simulation ---")
    
    try: 
        for i, ch in enumerate(reverse_char_generator(test_string_large_size)):
            # Stop early after first few characters to avoid massive memory output in demo
            if i > 50: break
            
            sys.stdout.write(ch)
            
            # Flush periodically to ensure visibility of stream
            sys.stdout.flush()

    except Exception as e:
        print(f"Error during large string processing: {e}")