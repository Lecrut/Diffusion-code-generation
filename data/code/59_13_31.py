def find_middle_value(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    sorted_numbers = sorted(numbers)
    mid_index = len(sorted_numbers) // 2
    
    return sorted_numbers[mid_index]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    middle_value = find_middle_value(sample_values)
    print(middle_value)