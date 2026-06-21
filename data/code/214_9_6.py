def find_smallest_value(number_list):
    if not number_list:
        raise ValueError("Input list is empty")
    smallest = number_list[0]
    for num in number_list[1:]:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_values = [7, 2, 5, 3, 1]
    result = find_smallest_value(sample_values)
    print(result)