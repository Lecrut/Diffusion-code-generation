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
    sample_data = [1, 8.5, 3, 10, 5, 2.1, 7, 4.9, 6, 0, 5.0]
    sorted_data = sort_mixed_numbers(sample_data)
    print(sorted_data)