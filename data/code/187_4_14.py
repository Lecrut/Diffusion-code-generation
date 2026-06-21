def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for value in data[1:]:
        if value > largest:
            largest = value
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))