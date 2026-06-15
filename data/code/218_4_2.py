def find_smallest(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    smallest = iterable[0]
    for item in iterable[1:]:
        if item < smallest:
            smallest = item
    return smallest
if __name__ == '__main__':
    data1 = (5, 2, 8, 1, 9)
    data2 = [42, 10, 33, 55]
    data3 = (100, 50, 75, 25)
    data4 = [99]
    data5 = []
    print(f"Smallest in {data1}: {find_smallest(data1)}")
    print(f"Smallest in {data2}: {find_smallest(data2)}")
    print(f"Smallest in {data3}: {find_smallest(data3)}")
    print(f"Smallest in {data4}: {find_smallest(data4)}")
    try:
        find_smallest(data5)
    except ValueError as e:
        print(f"Error for empty list: {e}")