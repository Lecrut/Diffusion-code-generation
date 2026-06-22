def find_middle_item(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    SAMPLE_LIST_ODD = [1, 3, 5, 7, 9]
    SAMPLE_LIST_EVEN = [2, 4, 6, 8, 10, 12]
    
    print(find_middle_item(SAMPLE_LIST_ODD))
    print(find_middle_item(SAMPLE_LIST_EVEN))