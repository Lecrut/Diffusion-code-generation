def find_min_max(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    return min(iterable), max(iterable)
if __name__ == '__main__':
    data1 = (5, 2, 9, 1, 7)
    print(f"Data: {data1}")
    min1, max1 = find_min_max(data1)
    print(f"Smallest: {min1}, Largest: {max1}")
    data2 = {10.5, -3.2, 0, 45.1}
    print(f"\nData: {data2}")
    min2, max2 = find_min_max(data2)
    print(f"Smallest: {min2}, Largest: {max2}")
    data3 = [100]
    print(f"\nData: {data3}")
    min3, max3 = find_min_max(data3)
    print(f"Smallest: {min3}, Largest: {max3}")
    data4 = ()
    try:
        find_min_max(data4)
    except ValueError as e:
        print(f"\nHandling empty iterable error: {e}")