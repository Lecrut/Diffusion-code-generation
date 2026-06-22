def find_min(lst):
    if not lst:
        return None
    current_min = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < current_min:
            current_min = lst[i]
    return current_min

if __name__ == '__main__':
    sample_data = [34, -1, 78, 2, 90, -5, 12]
    result = find_min(sample_data)
    print(result)