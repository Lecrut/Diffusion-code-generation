def find_minimum_generator(data):
    if not data:
        return
    current_min = data[0]
    yield current_min
    for element in data[1:]:
        if element < current_min:
            current_min = element
            yield current_min
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    minimum_generator = find_minimum_generator(sample_list)
    print("Minimum elements yielded:")
    for min_val in minimum_generator:
        print(min_val)