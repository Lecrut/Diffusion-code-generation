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
            pass
    greater_than_five.sort()
    less_than_or_equal_to_five.sort()
    return greater_than_five + less_than_or_equal_to_five
if __name__ == '__main__':
    sample_list = [3.5, 7, 1.2, 8.0, 5, 0, 9.9, 4, 5.0, 10]
    sorted_list = sort_mixed_numbers(sample_list)
    print(sorted_list)