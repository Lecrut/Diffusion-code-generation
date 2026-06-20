def find_middle_element(numbers):
    if not numbers:
        return "List is empty"
    length = len(numbers)
    mid_index = length // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(find_middle_element(sample_list))