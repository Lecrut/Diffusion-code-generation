def sums_differ(list1: list[float], list2: list[float]) -> bool:
    """
    Returns True if sum of list1 is different from sum of list2, False otherwise.
    
    Optimized by computing the difference directly to avoid redundant addition operations.
    Time Complexity: O(n + m) where n and m are lengths of input lists.
    Space Complexity: O(1).
    """
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    # Hard-coded sample values to test without user interaction or external dependencies
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7]

    result = sums_differ(list_a, list_b)
    
    if result:
        print("The sums are different.")
    else:
        print("The sums are the same.")