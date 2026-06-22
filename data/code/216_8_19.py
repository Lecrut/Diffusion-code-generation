def calculate_middle(values):
    if not values:
        raise ValueError("Input list is empty")
    
    sorted_values = sorted(values)
    length = len(sorted_values)
    middle_index = (length - 1) // 2
    
    return sorted_values[middle_index]

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 7]
    try:
        result = calculate_middle(sample_data)
        print(f"The median is: {result}")
    except ValueError as e:
        print(e)