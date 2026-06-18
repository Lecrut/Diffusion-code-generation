def reverse_by_adjacent_swaps(s: str) -> str:
    """
    Reverses a string by iteratively swapping adjacent characters until 
    the entire string is reversed in place (conceptually).
    
    This function simulates bubble sort logic where we repeatedly swap 
    adjacent elements to move each character from its original position 
    to its reverse-position. While not strictly necessary for correctness, 
    this demonstrates iterative adjacent swaps as requested.
    
    Args:
        s (str): The input string to be reversed using only adjacent swaps.
        
    Returns:
        str: A new string which is the reverse of the original input.
    """
    # Convert string to a list for mutability, though we return a copy anyway 
    # since strings are immutable in Python and modifying it directly isn't ideal 
    # without converting back. However, true "in-place" modification on an object 
    # like str is impossible; thus we operate on the underlying characters.
    
    chars = list(s)
    n = len(chars)
    
    # We perform passes similar to bubble sort: in each pass, move elements 
    # from their current position towards where they should end up in a reversed string.
    # For full reversal via adjacent swaps, we can simply iterate and swap if the 
    # element is not yet at its final target (which for reverse is n-1-i).
    
    swapped = True
    while swapped:
        swapped = False

if __name__ == '__main__':
    pass
