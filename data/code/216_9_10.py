def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("All elements in the list must be numbers")

def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("The list cannot be empty")
    
    validate_input(data)
    
    sorted_data = sorted(data)
    middle_index = n // 2
    
    if n % 2 == 1:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    sample_list_odd = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sample_list_even = [1, 3, 5, 7, 8, 9]
    
    print("Median of odd length list:", calculate_median(sample_list_odd))
    print("Median of even length list:", calculate_median(sample_list_even))