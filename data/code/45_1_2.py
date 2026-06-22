def find_minimum(numbers):
    if not numbers:
        return None
    current_min = numbers[0]
    index = 1
    list_length = len(numbers)
    while index < list_length:
        candidate = numbers[index]
        if candidate < current_min:
            current_min = candidate
        index += 1
    return current_min

if __name__ == '__main__':
    test_data = [88, 45, 22, 99, 11, 33, 7, 54, 19]
    minimum_value = find_minimum(test_data)
    print(minimum_value)