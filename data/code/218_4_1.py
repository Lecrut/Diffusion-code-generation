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
    result1 = find_smallest(data1)
    print(f"The smallest in {data1} is: {result1}")
    data2 = [42, 10, 55, 33]
    result2 = find_smallest(data2)
    print(f"The smallest in {data2} is: {result2}")
    data3 = (100, 99, 101)
    result3 = find_smallest(data3)
    print(f"The smallest in {data3} is: {result3}")
    data4 = [7]
    result4 = find_smallest(data4)
    print(f"The smallest in {data4} is: {result4}")