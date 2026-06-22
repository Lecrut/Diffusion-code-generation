def find_min_max(nested_list):
    if not nested_list:
        raise ValueError("Nested list cannot be empty")
    
    min_val = float('inf')
    max_val = float('-inf')

    for sublist in nested_list:
        if isinstance(sublist, list):
            sub_min, sub_max = find_min_max(sublist)
            min_val = min(min_val, sub_min)
            max_val = max(max_val, sub_max)
        else:
            raise ValueError("Sublists must contain only integers")

    return min_val, max_val

if __name__ == '__main__':
    data1 = [[5, 2], [9, 1, 7]]
    print(f"Data: {data1}")
    min1, max1 = find_min_max(data1)
    print(f"Smallest: {min1}, Largest: {max1}")

    data2 = [[[3.14, 1.618], [2.718]], [-5, 0, 10, -2]]
    print(f"\nData: {data2}")
    min2, max2 = find_min_max(data2)
    print(f"Smallest: {min2}, Largest: {max2}")

    data3 = [[], [100]]
    try:
        print(f"\nData: {data3}")
        min3, max3 = find_min_max(data3)
        print(f"Smallest: {min3}, Largest: {max3}")
    except ValueError as e:
        print(e)