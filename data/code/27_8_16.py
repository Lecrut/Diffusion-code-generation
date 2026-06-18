def sums_are_different(list1: list[float], list2: list[int]) -> bool:
    """
    Returns True if sum of numbers in list1 is different from sum of numbers in list2, False otherwise.
    
    Parameters:
        list1 (list): A list of float or int values.
        list2 (list): A list of int values.

    Returns:
        bool: True if sums differ, else False.
    
    Complexity: O(n + m) where n and m are lengths of the input lists respectively.
    """
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    # Sample inputs with hard-coded values (no user interaction required).
    list_a = [3, 5, -2]      # Sum: 6
    list_b = [7, 8]          # Sum: 15

    result = sums_are_different(list_a, list_b)

    print(result)   # Expected output: True (since 6 != 15)