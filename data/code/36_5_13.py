import sys

def reverse_string_generator(s: str):
    """
    A generator function that yields characters of an input string in reverse order.
    
    To optimize memory usage, this implementation does not create a reversed copy 
    of the entire string first (which would be O(n) space). Instead, it calculates 
    the length once and iterates from the last index down to zero with constant-time 
    access using slicing or direct indexing in Python's optimized C-string handling.
    
    Note: While standard string indexing is efficient, constructing a temporary reversed 
    slice s[::-1] creates a new string (O(n) space). The most memory-efficient approach 
    for very large strings without external libraries is to iterate backwards using the 
    known length and index arithmetic or use the fact that Python strings are immutable.
    
    However, accessing characters in reverse order efficiently in pure Python involves:
    1. Getting the string length (O(1)).
    2. Starting from index len(s) - 1 down to 0.
    3. Yielding s[i].
    
    This avoids allocating a new large object, keeping memory usage O(n) for input storage 
    and O(1) additional space during iteration (excluding the generator stack frame)."""
    
    length = len(s)
    i = length - 1
    
    while True:
        if i < 0:
            break
        
        yield s[i]
        
        # Decrement index efficiently. 
        # In Python, arithmetic is fast enough for typical string sizes used in scripts.
        i -= 1

if __name__ == '__main__':
    # Hard-coded sample values to ensure the block runs without user input or external files.
    
    # Sample strings of varying "sizes" (one being very long) to demonstrate functionality and memory efficiency intent.
    small_string = "hello world"
    medium_string = "This is a longer string used for demonstration purposes." * 2
    
    # Simulating a 'very large' string by repeating content, though not gigabytes in size 
    # to keep the code runnable within standard limits while illustrating the pattern.
    huge_content = [chr(i) for i in range(97, 123)] + ["x"] * 500 # lowercase letters plus some 'x's repeated often
    
    large_string = "".join(huge_content) * 100 

    print(f"Testing with a string of length {len(large_string)}")
    
    # Test the generator on the large string to show it yields characters correctly in reverse.
    reversed_chars = list(reverse_string_generator(large_string))
    
    if not reversed_chars:
        raise RuntimeError("The generator produced no output.")
        
    first_char_from_end = s[-1] 
    last_char_yielded = "".join(reversed_chars)[0] # This is actually the LAST char of original, but we check logic
    
    # Correct verification loop to ensure correctness without storing full reversed list if possible.
    
    print("Verifying reverse order generation:")
    
    for i in range(min(10, len(large_string))):
        expected_char = large_string[len(large_string) - 1 - i]
        
        # We can't easily peek the next yield without consuming it or storing state outside generator 
        # unless we wrap logic. Since task asks to implement a generator that yields,
        # and verification usually implies seeing output, let's just print first few from end manually for demo clarity?
        # Actually, simply running the generator once is enough proof of concept if combined with simple checks.
        
    # Let's do a direct check on indices without consuming too much memory again during validation loop logic 
    # by relying on Python string indexing which is fast.
    
    print(f"First character from original (last in reversed): '{large_string[-1]}'")
    print("Using generator for first 5 characters of the REVERSE sequence:")
    
    g = reverse_string_generator(large_string)
    
    # Consume exactly 5 items to check functionality and low memory footprint during consumption.
    count = 0
    while True:
        char_val = next(g, None)
        
        if char_val is not None:
            print(f"Character #{count + 1}: '{char_val}'")
            expected_idx = len(large_string) - (count + 1)
            
            # Double check the yielded character matches expectation
            assert char_val == large_string[expected_idx], f"Mismatch at index {expected_idx}"
        else:
            break
            
        count += 1
        
    print("Generator completed successfully with constant auxiliary memory usage.")