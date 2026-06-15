def find_range(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 4, 7, 1, 9]
    list3 = []
    list4 = [5]
    print(f"Range of {list1}: {find_range(list1)}")
    print(f"Range of {list2}: {find_range(list2)}")
    try:
        print(f"Range of {list3}: {find_range(list3)}")
    except ValueError as e:
        print(f"Error for {list3}: {e}")
    print(f"Range of {list4}: {find_range(list4)}")