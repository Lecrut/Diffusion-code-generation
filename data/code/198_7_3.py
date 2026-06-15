def find_smallest_generator(data):
    if not data:
        return
    smallest = data[0]
    yield smallest
    for item in data[1:]:
        if item < smallest:
            smallest = item
            yield smallest
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 7]
    generator = find_smallest_generator(sample_list)
    result = []
    for value in generator:
        result.append(value)
    print(result)