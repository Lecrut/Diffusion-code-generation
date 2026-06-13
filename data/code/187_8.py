def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(find_largest(list2))
    list3 = [7]
    print(find_largest(list3))
    list4 = []
    print(find_largest(list4))