from typing import List

def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where every character at an even index is swapped 
    with the character at the next odd index, and vice versa. If there are two adjacent characters, they are always swapped regardless of parity logic in this specific context (even-even or odd-odd).

    The implementation creates intermediate lists to handle swapping without side effects on input string state,
    ensuring purely functional behavior as requested.
    
    Args:
        s: Input string
    
    Returns:
        New string with characters at positions swapped based on the specified logic
    """
    result = []
    n = len(s)

    for i in range(n):
        if i + 1 < n and (i % 2 == 0 or i % 2 != 0):
            # Always swap adjacent pairs: index i with i+1
            if i % 2 == 0:
                result.append(s[i + 1])
                result.append(s[i])
            else:
                result.append(s[i - 1])
                result.append(s[i])
        elif i == n - 1 and (i % 2 != 0 or i == len(result)):
             pass

    # Correcting the logic to strictly follow "every character at an even index is swapped with 
    # the character at the next odd index, and vice versa" meaning adjacent pairs are always swapped.
    
    return "".join(reversed(s))

def swap_adjacent_pairs(s: str) -> str:
    """
    Correctly implements swapping every pair of characters (0-1, 2-3, etc.).
    """
    result = []
    n = len(s)

    for i in range(0, n, 2):
        if i + 1 < n:
            # Swap s[i] and s[i+1]
            result.append(s[i + 1])
            result.append(s[i])
    
    return "".join(result)

if __name__ == '__main__':
    test_strings = [
        "abcde",      # Expected: bacd e -> b a c d e (actually bc da ec? No, pairs swap) 
                     # 0(a)<->1(b), 2(c)<->3(d), 5(e) stays. Result: badce
        "hello world",# h<->e, l<->l, o<>w, r<y>?, d stays -> ehlol wry? No. 
                     # 0(h)-1(e)->eh, 2(l)-3(l)->ll (wait, swap means put next first), so el lh
        "Python"      # P-y-t-h-o-n -> yPthno (pairwise) => y-P h-T o-N n stays? No. 
                     # P<->y, t<->h, o<->n. Result: yPhotN
    
    ]

    for test in test_strings:
        print(f"Input: {test}")
        output = swap_adjacent_pairs(test)
        print(f"Output (Correct Pairwise Swap): {output}\n")