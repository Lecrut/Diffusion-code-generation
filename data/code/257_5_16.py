def find_largest_and_smallest(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    if not all(isinstance(i, (int, float)) for i in flat_list):
        raise ValueError("All elements must be integers or floats.")
    return max(flat_list), min(flat_list)

def calculate_difference(nested_list):
    largest, smallest = find_largest_and_smallest(nested_list)
    return largest - smallest

if __name__ == '__main__':
    sample_nested_list = [[10, 20], [30, 40, 50], [60]]
    difference = calculate_difference(sample_nested_list)
    print(difference)