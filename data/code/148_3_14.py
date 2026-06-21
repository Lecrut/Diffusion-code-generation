def find_largest(data):
    if not data:
        raise ValueError("List is empty")
    largest = data[0]
    for value in data:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 30]
    print(f"Largest in {list1}: {find_largest(list1)}")
    list2 = [-5, -1, -10, -2, -7]
    print(f"Largest in {list2}: {find_largest(list2)}")
    list3 = [3.14, 2.71, 1.618, 4.59, 5.73]
    print(f"Largest in {list3}: {find_largest(list3)}")