import timeit

def reverse_iterative(s):
    """Reverse a string iteratively using two pointers."""
    result = []
    start_idx = 0
    end_idx = len(s) - 1
    
    while start_idx <= end_idx:
        if start_idx == end_idx:
            result.append(s[start_idx])
            break
        
        # Append characters in reverse order directly to build the string
        # This avoids appending individual chars and reconstructing, 
        # but for pure iteration without list join optimization it's similar.
        # To make it truly iterative char-by-char from end is more efficient logically:
        
    # Resetting logic for clarity and directness as per "iterative using a loop" request
    result = []
    i = 0
    while i < len(s):
        j = len(s) - 1 - i

if __name__ == '__main__':
    pass
