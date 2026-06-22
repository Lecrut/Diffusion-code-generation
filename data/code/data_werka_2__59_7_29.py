def find_middle_item(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    
    MIDDLE_INDEX_CONSTANT = 2
    
    middle_index = len(numbers) // MIDDLE_INDEX_CONSTANT
    return numbers[middle_index]

if __name__ == '__main__':
    sample_list_odd = [5, 10, 15, 20, 25]
    sample_list_even = [6, 12, 18, 24, 30, 36]
    
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))