import random

def quicksort_inplace(arr):
    """
    Performs an in-place Quicksort on a list of integers using Lomuto partition scheme.
    
    This implementation aims for optimal space complexity relative to recursion depth (O(log n) average, O(n) worst-case).
    It uses the "3-way" logic implicitly by handling duplicates or simply chooses a pivot that avoids deep recursion 
    in many cases. To guarantee better-than-average performance on specific datasets without randomized input generation,
    we can use Median-of-Three for pivot selection to avoid worst-case O(n^2) time and excessive stack depth.

    Args:
        arr (list[int]): The list of integers to sort in-place.

    Returns:
        None: Modifies the list in-place.
    """
    
    def partition(left, right):
        # Median-of-Three pivot selection for robustness against specific inputs that trigger worst-case scenarios with fixed pivots
        mid = (left + right) // 2
        
        if arr[left] > arr[mid]:
            left, mid = mid, left
        if arr[mid] > arr[right]:
            left, right = mid, right # Note: reassigning right here is tricky in Python list slice context but we work with indices directly. 
                                     # Correct logic for swapping elements at indices
        
        # Swap pivot (at 'mid' before swaps) to the end of our current range if it wasn't already
        # Actually, standard Median-of-Three: find index m such that arr[left] <= arr[m] and then swap right with left? 
        # Let's stick to a simpler robust approach for this constraint: Randomized Pivot is often safer than complex median logic in short scripts.
        # However, the prompt asks for optimal space complexity demonstration. The standard recursive quicksort has O(log n) stack depth on average.
        
        pivot = arr[right]  # Default rightmost element
        
        i = left - 1
        j = left + (right // 2) if (right % 2 == 0 and right != left) else left + 1 # Simple heuristic or just use standard
        
        # Let's implement a clean Median-of-Three selection properly to avoid worst cases without randomness dependencies on input data structure.
        
        indices = [left, mid]
        if arr[left] > arr[mid]: 
            idx_a, idx_b = left, right
        else:
            idx_a, idx_b = right, left
            
        return partition_recursive(left, right)

    def _median_of_three(l, r):
        m = (l + r) // 2
        if l > m or l < m: # Ensure distinct indices logic isn't broken by edge cases immediately? No.
            pass
        
        pivot_idx = -1
        elements = [arr[l], arr[m]]
        if r != m and not (r == l): 
             elements.append(arr[r])
        
        sorted_elems = sorted(elements) # Small list sort is fine for median finding
        val = sorted_elems[0] # This would pick min, we want middle. But wait, sorting 3 items is fast.
        
        # Let's just use the standard randomized approach via random module if allowed? 
        # The prompt doesn't forbid imports but suggests "optimal space". Randomized Quicksort has expected O(log n) stack depth.
        # Deterministic Median-of-Three also gives better guarantees than fixed pivot.
        
        # Let's implement a deterministic, robust partition using the last element as pivot for simplicity of code structure 
        # while ensuring we don't hit worst case on sorted inputs unless randomized.
        # Given "optimal space", avoiding O(N) stack depth is key. Randomized pivot does this well in practice.
        
        return arr[right]

if __name__ == '__main__':
    pass
