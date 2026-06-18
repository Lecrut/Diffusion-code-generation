import time

def compare_and_report(list_a: list[int], list_b: list[int]) -> dict[str, int]:
    """
    Compares two lists of integers by their sum and returns a dictionary
    containing the sums and identifying which list is larger.

    Args:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.

    Returns:
        dict[str, int]: A dictionary with keys 'sum_a', 'sum_b', 
                       and 'winner' (either 'A' or 'B').
    
    Time Complexity: O(n + m) where n is the length of list_a and m is the length of list_b.
    Space Complexity: O(1).
    """
    sum_a = 0
    for num in list_a:
        sum_a += num
    
    sum_b = 0
    for num in list_b:
        sum_b += num

    if sum_a > sum_b:
        winner = 'A'
    elif sum_b > sum_a:
        winner = 'B'
    else:
        winner = 'TIE'

    return {
        "sum_a": sum_a,
        "sum_b": sum_b,
        "winner": winner
    }

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, network access, or pre-existing files used.
    
    list_sample_a = [10, 20, -5, 3]
    list_sample_b = [40, -2, 1]

    start_time = time.perf_counter()
    result = compare_and_report(list_sample_a, list_sample_b)
    end_time = time.perf_counter()

    print("Comparison Results:")
    print(f"Sum of List A: {result['sum_a']}")
    print(f"Sum of List B: {result['sum_b']}")
    print(f"Winner: {result['winner']}")
    
    if result["winner"] != "TIE":
        winning_list = 'List A' if result['winner'] == 'A' else 'List B'
        print(f"The list with the larger sum is: List ({winning_list})")

    execution_time_ms = (end_time - start_time) * 1000
    print(f"Execution time for comparison: {execution_time_ms:.6f} ms")