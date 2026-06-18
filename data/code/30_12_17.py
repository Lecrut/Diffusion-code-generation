import sys

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the input string.
    
    If the length is odd, the last character remains unchanged.
    Optimized using list comprehension for Pythonic efficiency on large strings.
    """
    return "".join(s[i:i+2][::-1] if (i + 1) < len(s) else s[i:] 
                   for i in range(0, len(s), 2))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [
        "hello",      # Expected: olleh (h stays) -> wait, h-e-llo -> e-l-h-o? Let's trace manually.
                     # Input: h e l l o
                     # i=0: s[0:2] is 'he', reversed is 'eh'. Remaining from index 2: 'llo'
                     # Result so far: 'ehllo'? No, let's re-evaluate the logic.
    ]
    
    # Correct manual trace for "hello":
    # Indices: 0(h), 1(e), 2(l), 3(l), 4(o)
    # i=0: swap s[0] and s[1] -> 'eh' + rest('llo') = 'ehllo'? 
    # Wait, the previous logic in my head was slightly off. Let's stick to the code implementation which is standard.
    # Code logic: range(0, 5, 2) -> i=0, i=2.
    # i=0: s[0:2] = "he", reversed = "eh". Next part starts at index 2 ("llo").
    # The generator expression does: for each chunk of 2, reverse it and join. 
    # If odd length last char is taken as a single char slice (i+1 >= len), which returns s[i:].
    # i=0: "he" -> "eh". Remaining string from index 2? No, the generator doesn't handle accumulation of remaining manually outside loop.
    # Let's re-read my code logic carefully.
    # "".join(s[i:i+2][::-1] if (i + 1) < len(s) else s[i:] for i in range(0, len(s), 2))
    # If length is odd:
    # i=0: "he" -> "eh". 
    # i=2: s[2:4] = "ll", reversed "ll". Next part? The condition (i+1) < len checks if there's a second char.
    # At i=2, index 3 is 'l', index 4 is 'o'. So i+1(3) < 5 is True. Slice s[2:4] is "ll". Reversed "ll". 
    # Wait, what about the last character?
    # The loop stops at len(s)-step=5-2=3 (exclusive), so i takes values 0 and 2.
    # At i=2: slice s[2:4] is "ll", reversed is "ll". 
    # What happens to 'o' at index 4? It is never processed because the loop stops before reaching it, 
    # UNLESS we handle the tail differently or adjust range/condition.
    
    # Correction on implementation logic for odd length:
    # If I use s[i:i+2][::-1], and i=0 ("he"->eh), i=2 ("ll"->ll). Result "ehllo". The last 'o' is missing? 
    # Ah, the slice s[4:] would be needed. But my condition (i+1) < len(s) ensures we take pairs.
    # If length is odd, the last character is left out by this specific generator pattern if not handled explicitly for the remainder.
    
    # Let's refine the function to ensure 100% correctness without relying on potential edge-case bugs in mental derivation:
    # Standard approach: iterate with step 2. Append reversed pair. If remaining length > 0, append it (it will be single char).
    
    def swap_adjacent_chars_correct(s):
        result = []
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                # Swap adjacent characters
                pair = s[i] + s[i+1]
                result.append(pair[::-1])
                i += 2
            else:
                # Last character remains as is (or odd length tail)
                result.append(s[i:]) 
                break
        return "".join(result)

    # Re-implementing the optimized one-liner version correctly for clarity and robustness in final output.
    
    def swap_adjacent_chars_final(s: str) -> str:
        """Swaps every pair of adjacent characters."""
        chars = list(s)
        n = len(chars)
        result = []
        i = 0
        while i < n - 1:
            # Swap current and next, add to result immediately or build string? 
            # Building a new list is efficient.
            pair_start_idx = i
            pair_end_idx = i + 2
            # Actually simpler logic: just slice by 2 from the start of remaining part? No, that's O(N^2) if we do slicing repeatedly on strings (though small overhead here). 
            # List approach is best.
            
            # Swap chars[i] and chars[i+1], then append to result list
            temp = chars[i]
            chars[i] = chars[i+1]
            chars[i+1] = temp
            
            i += 2
        
        return "".join(chars)

    # Wait, modifying in place is O(N), which is optimal. 
    # But the requirement says "swaps every pair". In-place swap modifies original list.
    # Let's verify: "hello" -> indices 0,1 swapped (e,h). Then 2,3 swapped (l,l same). Index 4 left alone.
    # Result: ehll o? 
    # h e l l o
    # Swap(0,1): e h ...
    # Swap(2,3): l l ... (no change)
    # Final: e h l l o -> "ehllo". Correct for manual trace.
    
    # However, the previous generator logic I wrote earlier was flawed regarding odd tails if not careful. 
    # The in-place swap is safer and very clear.

    def robust_swap(s):
        lst = list(s)
        n = len(lst)
        i = 0
        while i < n - 1:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 2
        return "".join(lst)

    # Let's run the sample "hello" with robust_swap.
    # Input: h e l l o (len 5)
    # i=0: swap(0,1). List becomes [e, h, l, l, o]. i -> 2.
    # i=2: swap(2,3). List becomes [e, h, l, l, o] (l,l same). i -> 4.
    # Loop ends because n-1 = 4, condition i < 4 is false for i=4? No, 4 < 4 is False. 
    # Wait, range(0, n-1, 2) covers 0 and 2. Correct.
    
    test_str = "hello"
    expected_manual = "ehllo" # Based on h-e swap -> e-h; l-l no change. Last 'o' untouched.
    
    # Let's double check the prompt requirement: "swaps every pair of adjacent characters".
    # Does it mean (0,1), then (2,3)...? Yes, standard interpretation.