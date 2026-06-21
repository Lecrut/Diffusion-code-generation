def find_range(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return min(data), max(data)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    list3 = [10]
    try:
        print(f"Range of {list1}: {find_range(list1)}")
        print(f"Range of {list2}: {find_range(list2)}")
    except ValueError as e:
        print(e)
    print(f"Range of {list3}: {find_range(list3)}")