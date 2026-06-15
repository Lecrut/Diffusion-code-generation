def find_min_max(data):
    if not data:
        return
    min_val = data[0]
    max_val = data[0]
    for x in data[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    yield min_val
    yield max_val
if __name__ == '__main__':
    large_list = [3.14, 1.618, 2.718, 0.577, 99.9, -100.5, 42]
    min_max_generator = find_min_max(large_list)
    print("Minimum and Maximum values:")
    for value in min_max_generator:
        print(value)