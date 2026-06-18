import sys

def reverse_string_in_place(s: str) -> None:
    """
    Reverses a string in place by converting it to a list of characters,
    swapping from both ends towards the center, and joining back into a string.
    
    This approach minimizes memory usage relative to creating new strings or copies
    because it only holds the character list internally (which is necessary for 
    mutability) rather than allocating intermediate reversed strings. In Python, 
    immutable strings are not truly mutable without allocation, so this function 
    operates on a temporary list which is then converted back to a single result string.
    
    Note: True in-place modification of an immovable type like str requires the object 
    itself if passed as a bytearray or similar mutable buffer. For standard str input, 
    we convert to list for mutability (standard Python behavior), perform swaps, and return.
    Since strings are immutable objects, returning a new string is the idiomatic efficient way
    unless specifically using bytes/bytearray where true in-place mutation on the object reference isn't possible anyway without reassignment.
    
    However, to strictly adhere to "in place" logic conceptually:
    We will use bytearray for actual memory efficiency as it allows true byte-by-byte swapping 
    and avoids string decoding overhead if we were dealing with bytes directly (though input is str here).
    
    Approach chosen:
    1. Convert the input string to a list of characters (O(N) space, minimal constant factor compared to slicing copies repeatedly).
    2. Perform two-pointer swap traversal from start and end moving inward until they meet or cross.
    3. Join the reversed character list into a new single string object. This is O(N) time and one extra allocation of size N (plus input buffer), which is optimal for Python strings due to immutability constraints in CPython without using specialized buffers like bytearray from start if possible, but since we accept str, this is standard efficient practice.
    
    If strict zero-allocation beyond the necessary character list isn't feasible with immutable str semantics outside of a custom allocator (which is out of scope for general Python), 
    this remains the most memory-conscious algorithmic approach using available language features.
    """
    # Convert string to mutable sequence of characters
    char_list = list(s)
    
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap characters at pointers
        char_list[left], char_list[right] = char_list[right], char_list[left]
        
        # Move inward
        left += 1
        right -= 1
        
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    sample_strings = [
        "hello world",
        "Python is awesome!",
        "",
        "A"
    ]
    
    for original in sample_strings:
        reversed_str = reverse_string_in_place(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")