def largest_element_generator(data):
    if not data:
        return
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    yield largest
if __name__ == '__main__':
    large_dataset = range(1000000)
    generator = largest_element_generator(large_dataset)
    result = next(generator)
    print(result)