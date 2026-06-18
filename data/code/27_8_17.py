import sys
from functools import reduce
from operator import add

def sums_differ(list1: list[float], list2: list[int]) -> bool:
    """
    Returns True if sum of `list1` is different from sum of `list2`.
    
    Optimized for large inputs by using Python's built-in sum() which 
    utilizes C-level loops and memory-efficient iteration, avoiding explicit 
    Python-level reduce or manual accumulation loops.

    Args:
        list1 (list[float]): First list of numbers. Supports floats/integers.
        list2 (list[int]): Second list of integers.

    Returns:
        bool: True if sum(list1) != sum(list2), False otherwise.
    
    Complexity Analysis:
        Time: O(n + m) where n and m are lengths of the lists. Python's 
               built-in `sum()` is implemented in C and highly optimized.
        Space: O(0) auxiliary (input list modifications not performed)."""

    # Calculate sum for first list using efficient built-in function
    sum1 = sum(list1, 0.0 if isinstance(list1[0], float) else 0)
    
    # Calculate sum for second list using efficient built-in function
    sum2 = sum(int(x) for x in list2)

    return sum1 != sum2

if __name__ == '__main__':
    sample_list1 = [1.5, 2.3, -0.8]
    sample_list2 = [6]

    result = sums_differ(sample_list1, sample_list2)
    
    if result:
        print("Sum of first list differs from sum of second list.")
    else:
        print("Sums are equal.")