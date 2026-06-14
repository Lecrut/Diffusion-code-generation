def min_max_generator(data):
    if not data:
        return
    current_min = data[0]
    current_max = data[0]
    for item in data[1:]:
        if item < current_min:
            current_min = item
        elif item > current_max:
            current_max = item
    yield current_min
    yield current_max
if __name__ == '__main__':
    large_dataset = range(1000000)
    min_max_gen = min_max_generator(large_dataset)
    print("Minimum:", next(min_max_gen))
    print("Maximum:", next(min_max_gen))