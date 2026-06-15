def largest_element_generator(data):
    if not data:
        return
    current_max = data[0]
    yield current_max
    for element in data[1:]:
        if element > current_max:
            current_max = element
            yield current_max
if __name__ == '__main__':
    large_dataset = range(1000000)
    print("Largest element from large dataset:")
    for num in largest_element_generator(large_dataset):
        print(num)