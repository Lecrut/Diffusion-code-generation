def find_minimum(values):
    current_min = values[0]
    next_candidate = values[0]
    index = 1
    total_items = len(values)
    while index < total_items:
        next_candidate = values[index]
        if next_candidate < current_min:
            current_min = next_candidate
        index += 1
    return current_min

if __name__ == '__main__':
    test_data = [42, 7, 19, 0, 85, 3, 66]
    output = find_minimum(test_data)
    print(output)