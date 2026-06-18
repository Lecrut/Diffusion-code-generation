def reverse_string_by_adjacent_swaps(s: str) -> str:
    """
    Reverses a string by iteratively swapping adjacent characters until 
    the entire string is reversed in place (simulated via list conversion).
    
    This approach converts the input string to a mutable list, performs swaps 
    from left to right moving each character one position closer to its final 
    reversed position, and then joins it back into a string.
    
    Args:
        s (str): The input string to be reversed using adjacent swaps only.
        
    Returns:
        str: A new string which is the reverse of the original input.
    """
    # Convert string to list for mutability as strings are immutable in Python
    char_list = list(s)
    
    n = len(char_list)
    
    # Iterate from left to right, swapping each character with its next neighbor 
    # until it reaches its correct position in the reversed sequence.
    # For a full reversal via adjacent swaps (like bubble sort logic), we can simply
    # swap every element at index i with index n-1-i directly if allowed by "iterative"
    # but strictly adhering to "swapping adjacent characters iteratively" means 
    # moving elements one step at a time. However, the most efficient way using ONLY
    # adjacent swaps to achieve reversal is essentially simulating bubble sort or 
    # simply swapping i with n-1-i if we consider each swap operation as atomic.
    # To strictly follow "swapping adjacent characters iteratively" without unnecessary moves:
    # We can perform a single pass where for every index i, we bring the character 
    # from position (n - 1 - i) to position i by swapping it with its left neighbor repeatedly?
    # No, that would be O(n^2). The task asks to reverse the string. 
    # A direct reversal is possible in O(n/2) swaps if we swap s[i] and s[n-1-i].
    # But does "swapping adjacent characters iteratively" imply a constraint on WHICH pairs?
    # Usually, this phrasing implies bubble-sort-like behavior or just that the mechanism 
    # must be an adjacent swap operation. Since any permutation can be achieved by adjacent swaps,
    # and we want to reverse it efficiently: swapping s[i] with s[n-1-i] is NOT an adjacent swap unless i+1 == n-1-i.
    # Therefore, a true implementation of "only by swapping adjacent characters iteratively" 
    # that guarantees reversal in O(n^2) worst case (like bubble sort logic to move elements home):
    
    for i in range(len(char_list)):
        target_index = len(char_list) - 1 - i
        
        if target_index <= i:
            break
            
        # Move the character at 'target_index' to position 'i' by swapping it leftwards.
        # However, moving one element all the way takes O(n). Total O(n^2).
        # Alternatively, we can just swap char_list[i] and char_list[target_index] 
        # IF they are adjacent? No, that's not always true for reversal logic directly.
        
        # Let's re-read carefully: "reverse of the original string, but only by swapping adjacent characters iteratively".
        # This implies the process must consist solely of operations where we swap char_list[j] and char_list[j+1].
        # To reverse efficiently while strictly using ONLY adjacent swaps (no jumping):
        # We can iterate from right to left. For each position i, ensure it holds the correct character 
        # by swapping with its neighbor if needed? Actually, simply iterating through half the string 
        # and swapping s[i] with s[n-1-i] is NOT an adjacent swap unless |i - (n-1-i)| == 1.
        
        # The most robust interpretation that satisfies "only by swapping adjacent characters":
        # Perform a standard bubble-sort-like pass or simply iterate i from 0 to n//2 and 
        # if we strictly cannot jump, we must move elements one step at a time? 
        # But moving element X from pos P to Q requires (P-Q) swaps. Total complexity O(n^2).
        
        # However, there is an optimization: If the goal is just reversal, can we do better than O(n^2)?
        # No, if restricted strictly to adjacent swap operations as atomic units without lookahead 
        # that skips steps? Actually, even with lookahead, swapping s[i] and s[n-1-i] directly violates 
        # "adjacent" unless they are neighbors.
        
        # Let's implement the O(n^2) approach which is safe: For each position i from 0 to n//2 - 1,
        # bring the character that belongs at i (which starts at n-1-i) to position i by swapping 
        # it with its left neighbor repeatedly.
        
        current_pos = target_index
        
        while current_pos > i:
            char_list[current_pos], char_list[current_pos - 1] = char_list[current_pos - 1], char_list[current_pos]
            current_pos -= 1
            
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies.
    test_cases = [
        "hello",
        "Python",
        "aabbccdd",
        "",
        "racecar"
    ]

    for s in test_cases:
        result = reverse_string_by_adjacent_swaps(s)
        print(f"Original: {s}")
        print(f"Reversed (via adjacent swaps): {result}\n")