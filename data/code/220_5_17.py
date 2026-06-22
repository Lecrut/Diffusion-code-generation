def calculate_average_of_elements(input_list):
    if not all(isinstance(subset, set) for subset in input_list):
        raise ValueError("All elements in the list must be sets.")
    
    total_sum = sum(sum(subset) for subset in input_list)
    total_count = sum(len(subset) for subset in input_list)
    
    if total_count == 0:
        return None
    
    average = total_sum / total_count
    return average

if __name__ == '__main__':
    sample_sets = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    
    try:
        result = calculate_average_of_elements(sample_sets)
        print(f"The average of all elements from the sets is: {result}")
    except ValueError as e:
        print(e)