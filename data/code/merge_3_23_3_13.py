import sys

def compare_sums_and_differences(list_a: list[int], list_b: list[int]) -> tuple[float, float]:
    """
    Calculates two metrics based on two input lists of numbers:
    
    1. The difference between the sum of elements in list_a and list_b (sum_a - sum_b).
    2. The absolute difference between the sums of their respective squares 
       (|sum_of_squares(list_a) - sum_of_squares(list_b)|).
       
    This function focuses on time complexity O(n + m), where n is the length of list_a
    and m is the length of list_b, as it iterates through both lists once.

    Args:
        list_a (list[int]): First list of numbers.
        list_b (list[int]): Second list of numbers.

    Returns:
        tuple[float, float]: A tuple containing:
            - The difference between the sums ((sum(list_a) - sum(list_b))).
            - The absolute difference between the sums of squares 
              (abs(sum_of_squares(list_a) - sum_of_squares(list_b))).
    
    Note on Complexity:
        Both lists are traversed a constant number of times (once for summation, once for square summation),
        resulting in linear time complexity O(n + m). Space complexity is O(1) as no additional 
        data structures proportional to input size are created.

    Example Usage (internal logic):
        Input: [1, 2], [3] -> Output difference = -4, Square sum diff abs = |6-9| = 3
    """
    
    # Calculate simple sums and the difference between them
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    sum_diff = sum_a - sum_b
    
    # Calculate squares of elements for each list separately (still O(n))
    sq_sum_a = 0.0
    for num in list_a:
        sq_sum_a += num * num
        
    sq_sum_b = 0.0
    for num in list_b:
        sq_sum_b += num * num
    
    # Calculate absolute difference between the squared sums
    abs_sq_diff = abs(sq_sum_a - sq_sum_b)

    return sum_diff, abs_sq_diff

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no external input needed)
    
    list_a_sample = [10, 20, 30]
    list_b_sample = [5, 15, 40]

    diff_sum, abs_diff_sq = compare_sums_and_differences(list_a_sample, list_b_sample)

    print(f"Sum difference (list a - list b): {diff_sum}")