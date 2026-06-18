import math

def compare_sums_and_lists(list_a: list, list_b: list) -> tuple[float, float]:
    """
    Calculates the difference between sums of two lists 
    and the absolute difference (sum of element-wise absolute differences).
    
    Args:
        list_a (list): First list of numbers.
        list_b (list): Second list of numbers.
        
    Returns:
        tuple[float, float]: 
            - sum_diff: Difference between sums of list_a and list_b.
            - element_abs_diff_sum: Sum of absolute differences of corresponding elements.
            
    Time Complexity: O(n) where n is the length of the shorter list (or both if equal).
    Space Complexity: O(1) excluding input/output storage.
    
    Note: If lists have different lengths, this function assumes they are padded 
    with zeros to match the length for comparison purposes as per standard numerical practices,
    unless specified otherwise in a specific problem context requiring explicit handling of mismatched sizes.
    However, based on typical interpretation without extra constraints here, we assume equal lengths or pad shorter list.
    
    Correction: To strictly adhere to 'absolute difference between lists' when they might differ in length,
    let's define it as sum(|a[i] - b[i]|) for all common indices i (up to min(len(a), len(b))).
    If the problem implies element-wise pairing beyond that without padding info, we take only up to minimum length.
    
    Revised approach: Compute sums over full lists and pairwise abs diff up to min length.
    """
    sum_a = 0
    for num in list_a:
        sum_a += float(num)

    sum_b = 0
    for num in list_b:
        sum_b += float(num)

    sum_diff = sum_a - sum_b

    # Compute element-wise absolute difference up to the minimum length of both lists
    common_length = min(len(list_a), len(list_b))
    
    abs_element_diff_sum = 0.0
    for i in range(common_length):
        val_a = float(list_a[i])
        val_b = float(list_b[i])
        diff = math.fabs(val_a - val_b)
        abs_element_diff_sum += diff

    return sum_diff, abs_element_diff_sum

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no user input required)
    list_a_sample = [10, 20, 30]
    list_b_sample = [5, 15, 40]

    sum_difference, element_diff_sum = compare_sums_and_lists(list_a_sample, list_b_sample)

    print(f"Sum Difference: {sum_difference}")
    print(f"Absolute Element-wise Difference Sum: {element_diff_sum}")