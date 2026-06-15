def find_min_max(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    return min(iterable), max(iterable)
if __name__ == '__main__':
    sample1 = (5, 2, 9, 1, 5)
    print(f"Sample 1: {sample1}")
    min1, max1 = find_min_max(sample1)
    print(f"Min: {min1}, Max: {max1}")
    sample2 = {'apple', 'zebra', 'banana', 'cat'}
    print(f"\nSample 2: {sample2}")
    min2, max2 = find_min_max(sample2)
    print(f"Min: {min2}, Max: {max2}")
    sample3 = [3.14, 1.618, 2.718]
    print(f"\nSample 3: {sample3}")
    min3, max3 = find_min_max(sample3)
    print(f"Min: {min3}, Max: {max3}")
    sample4 = (100,)
    print(f"\nSample 4: {sample4}")
    min4, max4 = find_min_max(sample4)
    print(f"Min: {min4}, Max: {max4}")
    try:
        empty_sample = ()
        print(f"\nSample Empty: {empty_sample}")
        find_min_max(empty_sample)
    except ValueError as e:
        print(f"Error caught for empty iterable: {e}")