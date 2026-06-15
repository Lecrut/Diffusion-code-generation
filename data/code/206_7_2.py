def find_min_generator(data):
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
    print("List 1:", list1)
    print("Min elements from List 1:")
    for min_val in find_min_generator(list1):
        print(min_val)
    list2 = [100, 50, 200, 10]
    print("\nList 2:", list2)
    print("Min elements from List 2:")
    for min_val in find_min_generator(list2):
        print(min_val)
    list3 = [7]
    print("\nList 3:", list3)
    print("Min elements from List 3:")
    for min_val in find_min_generator(list3):
        print(min_val)
    list4 = []
    print("\nList 4:", list4)
    print("Min elements from List 4:")
    for min_val in find_min_generator(list4):
        print(min_val)