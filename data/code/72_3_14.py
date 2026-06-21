def find_greater_pairs(list_first, list_second):
    max_index = min(len(list_first), len(list_second))
    matches = []
    for idx in range(max_index):
        current_first = list_first[idx]
        current_second = list_second[idx]
        if current_first > current_second:
            matches.append((current_first, current_second))
    return matches

if __name__ == '__main__':
    source_data = [20, 15, 30, 5]
    target_data = [10, 20, 25, 10]
    greater_items = find_greater_pairs(source_data, target_data)
    for val1, val2 in greater_items:
        print(f"{val1} > {val2}")