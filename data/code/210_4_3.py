def find_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return (minimum, maximum)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8]
    list2 = [10]
    list3 = []
    list4 = [-5, 0, 100]
    print(f"Range of {list1}: {find_range(list1)}")
    print(f"Range of {list2}: {find_range(list2)}")
    print(f"Range of {list3}: {find_range(list3)}")
    print(f"Range of {list4}: {find_range(list4)}")