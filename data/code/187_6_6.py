def largest_element_generator(data):
    if not data:
        return
    largest = data[0]
    yield largest
    for item in data[1:]:
        if item > largest:
            largest = item
    yield largest
if __name__ == '__main__':
    large_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    generator = largest_element_generator(large_list)
    print("Largest elements yielded:")
    for element in generator:
        print(element)
    another_list = [100, 50, 200, 10]
    generator2 = largest_element_generator(another_list)
    print("\nLargest elements yielded for another list:")
    for element in generator2:
        print(element)
    empty_list = []
    generator3 = largest_element_generator(empty_list)
    print("\nLargest elements yielded for an empty list:")
    for element in generator3:
        print(element)