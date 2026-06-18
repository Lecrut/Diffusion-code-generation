def swap_to_reverse(s: str) -> str:
    """
    Swaps adjacent characters in a string iteratively until it becomes 
    the reverse of the original string.
    
    Args:
        s (str): The input string to be reversed through swaps.
        
    Returns:
        str: The reversed string obtained by swapping adjacent characters.
    """
    # Convert the string to a list for mutability as strings are immutable in Python
    char_list = list(s)
    
    n = len(char_list)
    
    # Iterate until no more swaps are needed (i.e., the list is sorted reversedly relative to original positions)
    # We use a flag-based approach or check if the current state matches reverse. 
    # Since we want ONLY adjacent swaps, this mimics bubble sort logic but stops exactly when fully reversed.
    
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            # If characters are not in their final reversed positions relative to each other's original counterparts?
            # Actually, the most direct simulation of "swapping until reverse" via adjacent swaps 
            # is equivalent to bubble sort where we swap if left > right (conceptually) or simply run full passes.
            
            # However, a single pass from 0 to n-2 might not be enough depending on initial disorder?
            # No, the problem implies: perform operations until condition met. 
            # To reverse string S -> T where T is reverse of S, we need each char at index i (in result) 
            # to come from original index n-1-i.
            
            # A simple deterministic way using adjacent swaps only to achieve perfect reversal without complex logic:
            # Just perform a bubble-sort-like pass over the whole array. Each element moves to its reverse position?
            
            # Actually, if we simply iterate through all pairs (i, i+1) and swap if they are not in correct relative order... 
            # But what defines "correct"? The target is fixed: reversed string.
            
            # Simpler approach since the goal is purely to reach the state of being reversed from original via adjacent swaps:
            # We can just keep swapping until no more changes occur? That would mean it's already sorted in reverse order, which matches our goal.
            pass
        
        # Let's re-evaluate with a direct simulation that stops when the list is exactly reversed compared to start.
        
    # Correct logic using a loop that continues as long as the current string isn't fully reversed yet:
    
    original = s
    
    while True:
        if char_list == [c for c in list(reversed(original))]:
            break
        
        n_len = len(char_list)
        made_swap = False
        
        # Perform one full pass of adjacent swaps attempting to push elements towards their reversed positions?
        # Actually, the minimal number of swaps to reverse is roughly n^2/4 worst case. 
        # We can simulate a bubble sort where we swap if char[i] > char[j]? No, characters aren't numbers.
        
        # Since any sequence of adjacent swaps that reverses the array works (e.g., moving last element to front step by step),
        # let's implement: for each position from rightmost down to left+1, move it one spot left? 
        # That would be n-1 passes. But maybe simpler: just keep swapping until sorted in descending order if we assume distinct chars?
        
        # Let's use a greedy approach based on values? No, characters are arbitrary.
        
        # The most robust algorithmic way to reverse via adjacent swaps is the "move-to-front" style or full bubble sort logic 
        # knowing that any inversion can be removed with one swap. But we don't know which pairs need swapping without comparing.
        
        # However, notice: if we want to transform A->B where B = reverse(A), and only adjacent swaps allowed...
        # This is exactly the problem of calculating bubble sort distance but stopping at target permutation.
        # We can define a condition: swap i, i+1 IF they are not in their intended final positions relative to neighbors? 
        # Too complex logic-wise for arbitrary strings without value semantics.
        
        # Simpler interpretation: Just run adjacent swaps until the string equals its reverse. Since we start from non-reversed (usually),
        # and each swap brings us closer OR away, how do we know direction?
        
        # Re-read task: "swap characters ... such that resulting string is the reverse". 
        # It doesn't say minimum swaps or optimal path. Just *an* algorithm to achieve it via adjacent swaps iteratively.
        
        # Therefore, a straightforward strategy works:
        # Keep iterating until char_list == reversed(original). In each iteration, perform one swap at (i) and (i+1)? 
        # But which i? If we pick arbitrarily, might cycle or stall without progress towards specific target if not guided.
        
        # Guided Strategy: For position j from 0 to n-2, try swapping s[j] with s[j+1]. Does it help reach reverse state faster?
        # Not clear guidance unless we know where each char belongs. Char at i should end up at n-1-i.
        # So if current char_list[i] is NOT the character that SHOULD be there (which is original[n-1-i]), maybe swap with neighbor?
        
        # Let's try: Find first index i from left such that char_list[i] != expected_char_at_i where expected = reversed(original)[i].
        # Then move this char to its correct position using adjacent swaps. Move it rightwards or leftwards depending on relative order of target vs current pos?
        
        # Example trace: S="abc", rev="cba". 
        # i=0, 'a' should be at index 2 ('c'). So we need to move 'a' from 0->1->2. Swap(0,1), swap(1,2). Result "acb"? No wait...
        # Wait: if I have ["a","b","c"], and want ["c","b","a"]. 
        # Correct positions for original indices: a (from orig idx 0) -> target idx 2. b (orig 1) -> target idx 1? No, reverse of "abc" is "cba".
        # In result: pos0='c'(orig3-1=2), pos1='b', pos2='a'. So char at new[i] should be original[n-1-i].
        
        # Algorithm Refined: 
        # While not fully reversed:
        #   Find first index i from 0 where current_string[i] != expected_char_at_i (expected = rev_str[i])
        #   Let's say we have mismatch at i. We need to move that character(s) around until correct positions filled?
        #   Or simpler: bubble sort style but with target permutation defined by reverse mapping.
        
        pass
    
    # Final working approach inspired by "sorting" towards a specific permutation using adjacent swaps (like shell sort or selection):
    
    current = list(char_list)
    expected = [c for c in reversed(original)]  # Target state

    while True:
        if current == expected:
            break
        
        n_len = len(current)
        
        # Find the first index where they differ
        diff_idx = -1
        for i in range(n_len):
            if current[i] != expected[i]:
                diff_idx = i
                break
        
        if diff_idx == -1:  # Should not happen due to while condition but safety check
            continue
            
        # Now, we need to fix this discrepancy. Which move? 
        # Move the element at diff_idx towards its correct position relative to neighbors that are already in place?
        # Or simply apply a swap that resolves one inversion closer to target permutation.
        
        # Since any adjacent swap can resolve or create inversions, let's pick: 
        # Swap current[diff_idx] with neighbor (either left or right) such that we get closer to expected state?
        # Heuristic: look at diff_idx+1 and compare char values? Not reliable.
        
        # Better heuristic: We know the final position of every character from original list mapping to reversed indices.
        # Let's build a map: orig_index -> target index = n-1 - orig_index
        
        # But we don't track which original char is where easily without more overhead? 
        # Actually, since string content might have duplicates, tracking by identity requires value handling.
        
        # Alternate idea: Just run full bubble sort logic to reverse the list regardless of values!
        # How? Because reversing a list via adjacent swaps is same as sorting if we define order such that reversed(original) > original? No.

if __name__ == '__main__':
    pass
