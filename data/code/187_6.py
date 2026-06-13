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
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Largest elements from sample list:")
    for num in largest_element_generator(sample_list):
        print(num)
    large_sample = [100, 50, 200, 10, 300, 150]
    print("\nLargest elements from large sample list:")
    for num in largest_element_generator(large_sample):
        print(num)
    empty_list = []
    print("\nLargest elements from empty list:")
    for num in largest_element_generator(empty_list):
        print(num)