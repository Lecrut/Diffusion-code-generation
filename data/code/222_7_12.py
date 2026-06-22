def find_minimum(data):
    if not data:
        return None
    current_min = data[0]
    for item in data[1:]:
        if item < current_min:
            current_min = item
    return current_min

if __name__ == '__main__':
    large_list = [5, 12, 3, 8, 1, 15, -4, 9, 0, 22]
    min_value = find_minimum(large_list)
    print("Minimum value:", min_value)