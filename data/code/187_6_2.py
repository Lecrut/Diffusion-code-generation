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
    large_list = list(range(1000000))
    generator = largest_element_generator(large_list)
    print("Elements yielded by the generator:")
    for num in generator:
        print(num)