def find_middle_item(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_odd_length_list = [5, 10, 15, 20, 25]
    sample_even_length_list = [3, 6, 9, 12, 15, 18]
    print(find_middle_item(sample_odd_length_list))
    print(find_middle_item(sample_even_length_list))