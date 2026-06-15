def largest_element_generator(data):
    if not data:
        return
    largest = data[0]
    yield largest
    for element in data[1:]:
        if element > largest:
            largest = element
    yield largest
if __name__ == '__main__':
    large_list = [3, 1, 4, 1, 5, 9, 2, 6, 8, 7]
    generator = largest_element_generator(large_list)
    print("Elements yielded by the generator:")
    for item in generator:
        print(item)