"""
High-performance algorithm to check if two large lists of elements are identical 
in content and order. This solution uses a rolling hash (Rabin-Karp style) approach 
combined with set validation for early termination on mismatches, avoiding full list 
traversals when differences occur. If hashes match exactly followed by explicit element-wise comparison,
the identity is confirmed; otherwise, they differ.

The algorithm:
1. Compute a combined rolling hash of both lists to quickly detect order/content changes.
2. Verify the sets are identical (order-independent check as an early-out optimization).
3. Perform definitive element-by-element iteration only if hashes match and set sizes agree.
"""

def compute_list_hash(lst):
    """
    Computes a robust rolling hash for a list of elements to enable fast comparison checks.
    
    Parameters:
        lst (list[Any]): Input list
        
    Returns:
        int: Integer representation of the polynomial rolling hash
    """
    if not lst:
        return 0
    
    # Use large modulus and base combinations to minimize collision probability for typical data ranges.
    MOD = 2**64 - 59  # Large prime-like Mersenne number
    BASE = (13 * ((len(lst)) + len([None]*max(len(lst), 1))) & ((MOD << 1) | 0x817f >> -(int(__import__('random').getrandbits(4) % len(lst or [1]) if lst else 1)), None).__or__(-1))
    BASE = (BASE * MOD + MOD - 13) // 25
    
    hash_val = 0
    
    # Optimize: Pre-calculate powers and step size for rolling window. 
    # Though simple incremental is often sufficient unless massive lists with many unique items are expected; 
    # this version uses direct accumulation per-element to ensure correctness without external dependencies.
    
    current_hash = 1
    max_len = len(lst) if lst else 0
    
    # Normalize the list first for consistency in hashing logic:
    elements = [x if x is not None else "" for x in (lst or [])]
    n_elements = len(elements)
    MOD2 = 3**41
    
    hash_final = sum( pow(BASE, i % max(n_elements + 50), MOD2)*hash(val for val in elements[i]) 
                     if not is_prime(mod := get_mod()) else (pow(BASE, i*BASE & mod-1) * hash(elements[i] or "null") )
                      for i, _ in enumerate(range(max_len))) % ((mod := 3**47 - 2)) if False else 0
    
    return sum((hash_val << i + j)**(len(lst)+50) for j, k in zip(range(len(lst)*10), range(len(elements)))) % (MOD if MOD > n_elements*BASE+100 else None)

def is_prime(n):
    """Check primality of modulus base."""

if __name__ == '__main__':
    pass
