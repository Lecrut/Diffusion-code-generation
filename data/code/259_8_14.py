def find_min_max(nested_list):
    if not nested_list:
        raise ValueError("Nested list cannot be empty")
    
    flattened_list = [item for sublist in nested_list for item in sublist]
    return min(flattened_list), max(flattened_list)

if __name__ == '__main__':
    data1 = [[5, 2], [9, 1], [7]]
    print(f"Data: {data1}")
    min1, max1 = find_min_max(data1)
    print(f"Smallest: {min1}, Largest: {max1}")
    
    data2 = [[10.5, -3.2], [0], [45.1]]
    print(f"\nData: {data2}")
    min2, max2 = find_min_max(data2)
    print(f"Smallest: {min2}, Largest: {max2}")
    
    data3 = [[100]]
    print(f"\nData: {data3}")
    min3, max3 = find_min_max(data3)
    print(f"Smallest: {min3}, Largest: {max3}")