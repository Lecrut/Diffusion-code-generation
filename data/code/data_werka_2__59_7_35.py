def validate_input(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list')
    if not numbers:
        raise ValueError('The list cannot be empty')

def find_middle_item(numbers):
    validate_input(numbers)
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_list_odd = [5, 10, 15, 20, 25]
    sample_list_even = [3, 6, 9, 12, 15, 18]
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))