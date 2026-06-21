def validate_input(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements in the list must be integers.")

def find_kth_smallest(numbers, k):
    validate_input(numbers)
    if not (1 <= k <= len(numbers)):
        raise ValueError("k must be between 1 and the length of the list.")
    
    return sorted(numbers)[k-1]

if __name__ == '__main__':
    sample_numbers = [34, 78, 2, 56, 90]
    k = 3
    print(find_kth_smallest(sample_numbers, k))