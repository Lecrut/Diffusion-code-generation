import math

def compare_sums_and_lists(list_a: list, list_b: list) -> tuple[float, float]:
    """
    Compares two lists of numbers by calculating their respective sums and 
    returning both the difference between the sums and the absolute difference 
    between the lists themselves.

    Args:
        list_a (list): First list of numbers.
        list_b (list): Second list of numbers.

    Returns:
        tuple[float, float]: A tuple containing:
            - The difference between sum(list_a) and sum(list_b).
            - The absolute difference calculated as abs(sum(list_a) - sum(list_b)).
    
    Time Complexity: O(n), where n is the number of elements in the longer list.
    Space Complexity: O(1), excluding input storage.
    """
    # Calculate sums for both lists
    sum_a = 0
    for num in list_a:
        sum_a += num

    sum_b = 0
    for num in list_b:
        sum_b += num

    # Difference between the sums (sum_a - sum_b)
    diff_sums = sum_a - sum_b

    # Absolute difference is simply abs(diff_sums), but computed explicitly as requested 
    # to emphasize clarity and focus on absolute value logic.
    abs_diff_lists = abs(sum_a - sum_b)

    return diff_sums, abs_diff_lists

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are needed
    list_a_sample = [10, 20, 30]
    list_b_sample = [5, 15, 40]

    result_diff_sums, result_abs_diff_lists = compare_sums_and_lists(list_a_sample, list_b_sample)

    print(f"Difference between sums: {result_diff_sums}")
    print(f"Absolute difference between lists' sums: {result_abs_diff_lists}")