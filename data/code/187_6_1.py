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
    print("Largest elements from large list:")
    for item in largest_element_generator(large_list):
        print(item)
    empty_list = []
    print("\nLargest elements from empty list:")
    for item in largest_element_generator(empty_list):
        print(item)