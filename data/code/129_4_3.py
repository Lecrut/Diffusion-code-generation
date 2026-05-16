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
    sample_data = [1.5, 8.0, 3, 6.1, 5, 2.5, 10, 4.9, 5.0]
    sorted_data = sort_mixed_numbers(sample_data)
    print(sorted_data)