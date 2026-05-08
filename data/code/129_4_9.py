def sort_mixed_numbers(data):
    greater_than_five = []
    less_than_or_equal_to_five = []
    for item in data:
        if isinstance(item, (int, float)):
            if item > 5:
                greater_than_five.append(item)
            else:
                less_than_or_equal_to_five.append(item)
        else:
            less_than_or_equal_to_five.append(item)
    greater_than_five.sort()
    less_than_or_equal_to_five.sort()
    return greater_than_five + less_than_or_equal_to_five
if __name__ == '__main__':
    sample_list = [1, 8.5, 3, 10, 5, 4.9, 6, 0, 12.1, 5.0]
    sorted_list = sort_mixed_numbers(sample_list)
    print(sorted_list)