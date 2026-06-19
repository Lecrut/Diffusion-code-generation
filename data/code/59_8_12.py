def find_middle_item(numbers):
    length = len(numbers)
    middle_index = length // 2
    return numbers[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))