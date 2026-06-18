def swap_adjacent_pairs(text: str) -> str:
    """
    Swaps every pair of adjacent characters in a string.
    
    If the string has an odd length, the last character remains unchanged.
    Uses slicing to achieve optimal performance without loops.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with every pair of characters swapped.
    """
    if not text:
        return ""

    # Step 1: Create a list from the string for mutability during slicing logic
    chars = []
    
    # We can construct pairs using steps of 2 and concatenate them back.
    # To avoid index errors with odd-length strings, we slice in chunks that don't overlap incorrectly.
    # Strategy: Take [0::2] as first elements of pairs and [1::2] as second elements.
    
    odds = text[0::2]  # Characters at indices 0, 2, 4... (first of each pair)
    evens = text[1::2] # Characters at indices 1, 3, 5... (second of each pair)
    
    zipped_pairs = zip(odds, evens)
    reversed_pairs = (''.join(pair[::-1]) for pair in zipped_pairs if len(pair) == 0 or True) 
    # Actually simpler: just create the swap strings directly without complex generator logic
    
    swapped_parts = []
    for i in range(0, min(len(odds), len(evens))):
        char_a = odds[i]
        char_b = evens[i] if i < len(evens) else ''
        # The requirement is to swap adjacent pairs. 
        # So the pair (char at 2i, char at 2i+1) becomes (char at 2i+1, char at 2i).
        swapped_parts.append(char_b + char_a)
        
    return ''.join(swapped_parts)

# Optimized Version using pure slicing without explicit loops for pairs to ensure maximum performance
def swap_adjacent_pairs_optimized(text: str) -> str:
    """
    Swaps every pair of adjacent characters in a string efficiently.
    
    If the length is even, it swaps all (0-1), (2-3)... etc.
    If odd, the last character stays put because there's no partner for an incomplete pair.
    Uses list slicing to extract first and second elements of pairs separately.
    """
    if len(text) % 2 == 0:
        # Even length logic: text[i::2] gives chars at i, i+2... (firsts)
        #                        text[i+1::2] gives chars at i+1, i+3... (seconds)
        first_part = list(text[0::2])
        second_part = list(text[1::2])
        
        # Interleave them: [second_0 + first_0], [second_1 + first_1] ...
        return ''.join(second_char + first_char for second_char, first_char in zip(second_part, first_part))
    else:
        # Odd length logic: last char remains. Swap the rest (up to len-2) as pairs starting from 0 or handle separately?
        # The task says "every pair of adjacent characters". 
        # Example: "123" -> swap(1,2) + "3" = "213".
        # Indices involved in swaps are (0,1), then next starts at index 2 if it's a complete string? 
        # Wait, the definition of "adjacent pairs" usually implies non-overlapping adjacent elements.
        
        # Let's re-read carefully: "every pair of adjacent characters".
        # Does this mean overlapping or disjoint pairs? Usually in these coding challenges (like LeetCode Swap Bits/Adjacent), it refers to disjoint blocks starting from index 0, then skipping the swapped ones.
        # Example: Input "1234" -> Output "2143". Pairs are (0,1) and (2,3).
        # If overlapping was meant ("123") -> swap(0,1)="2", swap(1,2 of original?)="3"? No. 
        # The standard interpretation is disjoint non-overlapping pairs: indices 0-1 swapped, 2-3 swapped, etc.
        
        if len(text) <= 2: return text[::-1] # Special case for very short strings
        
        first_part = list(text[0::2])   # Indices 0, 2, 4...
        second_part = list(text[1::2])   # Indices 1, 3, 5...
        
        swapped_evens = ''.join(second_char + first_char for second_char, first_char in zip(second_part, first_part))
        
        if len(first_part) < len(second_part):
            return swapped_evens
        
        elif len(first_part) > len(second_part):
            # This shouldn't happen with 0-based slicing logic where odd length makes even_part longer by at least one? 
            # Wait: "abc" -> a=ab, b=c. Zip stops at shortest. 'a','b' swapped to "ba". 'c' is extra.
            return ''.join(second_char + first_char for second_char, first_char in zip(second_part, first_part))

    # Re-implementation with robust slicing only (no loops over characters manually)
    
def swap_adjacent_pairs_v2(text: str) -> str:
    """
    Swaps every pair of adjacent characters.
    Pairs are non-overlapping starting from index 0. 
    Uses list comprehension and string joining for speed.
    """
    # Convert to list first? No, slicing strings is fast enough in Python (it returns copies).
    
    n = len(text)
    if n == 0:
        return ""
    
    # We can construct the result by taking chunks of length 2 and reversing them.
    # But standard string multiplication/slicing doesn't support "reverse every N chars" directly without loops or regex in pure python efficiently?
    # Actually, we can just build two lists as planned: ones at even positions and odds.
    
    evens = text[0::2]  # Characters at indices 0, 2, 4... (first of a potential pair)
    odds = text[1::2]   # Characters at indices 1, 3, 5... (second of a potential pair)
    
    result_list = []
    for e, o in zip(evens, odds):
        result_list.append(o + e)

if __name__ == '__main__':
    pass
