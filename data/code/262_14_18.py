def find_extremes(nested_list):
    if isinstance(nested_list, list):
        return min(find_extremes(item) for item in nested_list), max(find_extremes(item) for item in nested_list)
    else:
        return nested_list, nested_list

if __name__ == '__main__':
    sample = [[1, 2, [3]], 4, [5, [6, 7], 8]]
    smallest, largest = find_extremes(sample)
    print(f"Smallest: {smallest}, Largest: {largest}")