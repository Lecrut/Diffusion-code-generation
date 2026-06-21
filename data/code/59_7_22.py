def find_middle_item(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [15, 25, 35, 45, 55, 65]
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))