def find_minimum_generator(data):
    if not data:
        return
    current_min = data[0]
    yield current_min
    for item in data[1:]:
        if item < current_min:
            current_min = item
            yield current_min
if __name__ == '__main__':
    large_list = [5, 12, 3, 8, 1, 15, -4, 9, 0, 22]
    minimum_generator = find_minimum_generator(large_list)
    print("Minimum values yielded:")
    for min_val in minimum_generator:
        print(min_val)