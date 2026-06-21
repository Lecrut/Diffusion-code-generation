def find_minimum_element(items):
    if not items:
        raise ValueError("List cannot be empty")
    min_value = items[0]
    for item in items[1:]:
        if item < min_value:
            min_value = item
    return min_value

if __name__ == '__main__':
    sample_list = [4, 2, 9, 6, 3, 7]
    minimum_value = find_minimum_element(sample_list)
    print(minimum_value)