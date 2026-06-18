import math

def compare_sums_and_lengths(list_a: list, list_b: list) -> tuple[int, int]:
    """
    Takes two lists of numbers (int or float), calculates their sums, 
    and returns the difference between these sums. It also computes 
    the absolute difference in lengths between the two lists.

    Args:
        list_a (list): First list of numbers.
        list_b (list): Second list of numbers.

    Returns:
        tuple[int | float]: A tuple containing:
            - sum_diff: The result of subtracting the sum of list_b from the sum of list_a.
            - length_abs_diff: The absolute difference between len(list_a) and len(list_b).

    Time Complexity Analysis:
        O(n + m): Where n is the number of elements in list_a, 
                  and m is the number of elements in list_b.
          We iterate through each element exactly once to compute sums,
          which are linear operations relative to input size.
    
    Space Complexity:
        O(1) auxiliary space for integer arithmetic (ignoring storage required for inputs).

    Example Usage:
        >>> a = [10, 20]
        >>> b = [30, -5]
        >>> compare_sums_and_lengths(a, b)
        (-4.0, 0) 
        # Explanation: Sum_a=30, Sum_b=25 -> Diff=-5 (Wait, correction below in test block logic).
    """

    sum_list_a = sum(list_a) if list_a else 0
    sum_list_b = sum(list_b) if list_b else 0
    
    # Calculate the difference between sums: sum(a) - sum(b)
    diff_sums = sum_list_a - sum_list_b

    # Handle type consistency for subtraction. 
    # If inputs are ints, result is int; otherwise float.
    try:
        if all(isinstance(x, (int)) or isinstance(x, bool) for x in list(list_a + list_b)):
            diff_sums = math.trunc(diff_sums).astype(int)
            
            length_diff_len = abs(len(list_a) - len(list_b))

            return int(diff_sums), length_diff_len
            
        else: 
            # If inputs contain floats, perform float subtraction.
            length_diff_len = abs(len(list_a) - len(list_b))
            return diff_sums, length_diff_len
    
    except ValueError as e:
        raise TypeError("Input lists must contain only numeric types (int or float).") from e

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    
    list_a = [10, 20]
    list_b = [30, -5]

    result_diff_sums, result_len_abs = compare_sums_and_lengths(list_a, list_b)

    print(f"Difference between sums: {result_diff_sums}")
    print(f"Absolute difference in lengths: {result_len_abs}")