def run_length_encode(lst):
    if not lst:
        return []
    result = []
    current_value = lst[0]
    count = 1
    for i in range(1, len(lst)):
        if lst[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = lst[i]
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    compressed = run_length_encode(sample_list)
    print(compressed)