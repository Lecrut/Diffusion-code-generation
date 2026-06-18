import sys

def swap_adjacent_chars(characters):
    """
    Iterates through a list of characters representing a string, swapping 
    each character at index i with the one at index i+1 where valid.
    
    The function operates internally on the mutable list to ensure efficiency.

    Parameters:
        characters (list[str]): A list containing single-character strings.

    Returns:
        None; modifies the input list in-place and returns nothing explicitly, 
        though this module is structured so that callers may expect side effects.
    
    Note:
        For a string of length n, indices run from 0 to n-2 before swapping occurs.
        The last element remains unchanged as there is no adjacent pair involving it after i+1 check.
        
    Example:
        Input list ["h", "e", "l"] -> Output ["e", "l", "dummy_char_to_replace_last"]? No actually, we don't replace the tail blindly if not provided; however here we assume input length is sufficient to have pairs or last char doesn't participate. Let's be precise:
        
        For n elements, valid i are 0..n-2 (since i+1 < len). So for ["h", "e", "l"]: 
          i=0 -> swap("h","e") => ["e","h","l"]
          i=1 -> swap("h","l") => ["e","l","h"]
        """
    n = len(characters)
    # Iterate up to n-2 because we access characters[i+1] which must be within bounds (max index is n-1, so max i is n-2)
    for i in range(n - 1):
        char_i = characters[i]
        char_ip1 = characters[i + 1]
        
        # Swap logic: replace both positions simultaneously to avoid partial updates causing incorrect swaps later if we used temp variable inside loop incorrectly? Actually, direct swap is fine. But for clarity and correctness in mutable list without extra memory cost per iteration except temporary variables locally (which Python does automatically), let's do it efficiently by updating the same reference or using a local helper:
        
        characters[i] = char_ip1
        characters[i + 1] = char_i

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input, 
    # command-line arguments, network access, or pre-existing files.

    # Sample string as a list of single-character strings for mutability and efficiency reasons:
    initial_list = ["h", "e", "l", "o"]  # Represents "hello" but note we only swap valid adjacent pairs up to len-2

    print("Before swapping:", "".join(initial_list))

    # Perform the swaps as per task requirement
    swap_adjacent_chars(initial_list)

    print("After swapping:", "".join(initial_list))