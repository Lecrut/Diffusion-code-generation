def find_min_max(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    return min(iterable), max(iterable)
if __name__ == '__main__':
    data1 = (5, 1, 9, 3, 7)
    print(f"Data: {data1}")
    min1, max1 = find_min_max(data1)
    print(f"Smallest: {min1}, Largest: {max1}")
    data2 = {100, 50, 200, 10}
    print(f"\nData: {data2}")
    min2, max2 = find_min_max(data2)
    print(f"Smallest: {min2}, Largest: {max2}")
    data3 = (3.14, 1.618, 2.718)
    print(f"\nData: {data3}")
    min3, max3 = find_min_max(data3)
    print(f"Smallest: {min3}, Largest: {max3}")
    data4 = [ -5, 0, 10, -2]
    print(f"\nData: {data4}")
    min4, max4 = find_min_max(data4)
    print(f"Smallest: {min4}, Largest: {max4}")
    try:
        find_min_max(())
    except ValueError as e:
        print(f"\nError handling test: {e}")