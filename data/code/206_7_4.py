def find_minimum_generator(data):
    if not data:
        return
    current_min = data[0]
    yield current_min
    for element in data[1:]:
        if element < current_min:
            current_min = element
            yield current_min
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print("List 1:")
    for min_val in find_minimum_generator(list1):
        print(min_val)
    list2 = [10, 4, 15, 3, 20]
    print("\nList 2:")
    for min_val in find_minimum_generator(list2):
        print(min_val)
    list3 = [7]
    print("\nList 3:")
    for min_val in find_minimum_generator(list3):
        print(min_val)
    list4 = []
    print("\nList 4 (Empty):")
    for min_val in find_minimum_generator(list4):
        print(min_val)