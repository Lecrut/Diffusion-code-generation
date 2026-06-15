def largest_element_generator(data):
    if not data:
        return
    largest = None
    for item in data:
        if largest is None or item > largest:
            largest = item
    yield largest
if __name__ == '__main__':
    large_dataset = range(1000000)
    generator = largest_element_generator(large_dataset)
    result = next(generator)
    print(result)