def swap_adjacent(s: str) -> str:
    chars = list(s)
    result_chars = []
    i = 0
    while i < len(chars):
        if i + 1 < len(chars):
            # Take current and next character, reverse their order in the chunk
            pair_chunk = [chars[i], chars[i+1]]
            for c in reversed(pair_chunk):
                result_chars.append(c)
            i += 2
        else:
            # Last character stays alone if odd length string or even logic handles it via loop condition effectively by not accessing out of bounds but here simple append works too. 
            # Actually simpler Pythonic way without explicit while for clarity in concise script usually list slice with stride then join back. 
            result_chars.append(chars[i])
            i += 1
            
    return "".join(result_chars)

# Alternative purely functional style often preferred:
import itertools

def swap_adjacent_v2(s: str) -> str:
    chars = s
    # Group every two characters, reverse the groupings if needed? No.
    # Interleave approach is better for this specific "swap adjacent" task per pair logic but let's stick to simplest list manipulation request. 
    # The while loop above works. Let's rewrite more concisely using itertools zip_longest with reversed pairing or direct indexing which is very pythonic in built-in ways?
    
    # Concise index based swap:
    chars = s.split('')[0] if 'chars' not in dir() else list(s)
    res = [] 
    for i, c1 in enumerate(chars):
        j = i + 2
        while j < len(chars):
            pair_start_i, pair_end_j = (i//2)*2, ((j-2)//2)*2 # Too complex logic error prone above. 
    
    # Let's revert to the most reliable concise implementation: 
    chars_list = list(s)
    res_chars = []
    
    for i in range(0, len(chars_list), 1): # iterate every index but we need steps of 2 effectively? No, step is 2 if only processing pairs. But wait swap adjacent means (0,1)->(1,0), then next pair starts at 2. So stepping by 2.
        pass
    
    # Correct Pythonic Concise approach: 
    chars_list = list(s)
    new_chars = []

if __name__ == '__main__':
    pass
