def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers")

def calculate_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 != 0:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample_list2 = [7, 8, 5, 10, 3, 4, 9, 1]
    
    validate_input(sample_list1)
    print("Median of list1:", calculate_median(sample_list1))
    
    validate_input(sample_list2)
    print("Median of list2:", calculate_median(sample_list2))