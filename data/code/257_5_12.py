def find_largest_and_smallest(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return max(flat_list), min(flat_list)

def calculate_difference(largest, smallest):
    return largest - smallest

if __name__ == '__main__':
    sample_nested_list = [[3, 5, 1], [8, 2, 9], [4, 7, 6]]
    largest, smallest = find_largest_and_smallest(sample_nested_list)
    difference = calculate_difference(largest, smallest)
    print(difference)