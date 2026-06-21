def find_min_max(values):
    if not values:
        return None, None
    smallest = min(values)
    largest = max(values)
    return smallest, largest

if __name__ == '__main__':
    sample_values = [7, 3, 9, 2, 5]
    result = find_min_max(sample_values)
    print(f"Minimum: {result[0]}, Maximum: {result[1]}")
    empty_list_result = find_min_max([])
    print(f"Empty list Min: {empty_list_result[0]}, Max: {empty_list_result[1]}")