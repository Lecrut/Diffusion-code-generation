def find_smallest_generator(data):
    if not data:
        return
    smallest = data[0]
    yield smallest
    for element in data[1:]:
        if element < smallest:
            smallest = element
        yield smallest
if __name__ == '__main__':
    sample_list = [10, 5, 20, 3, 15, 2]
    generator = find_smallest_generator(sample_list)
    results = list(generator)
    print(results)