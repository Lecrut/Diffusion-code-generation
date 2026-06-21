def run_length_encode(lst):
    if not lst:
        return []
    result = []
    current = lst[0]
    count = 1
    for i in range(1, len(lst)):
        if lst[i] == current:
            count += 1
        else:
            if count > 1:
                result.append((count, current))
            else:
                result.append((1, current))
            current = lst[i]
            count = 1
    if count > 1:
        result.append((count, current))
    else:
        result.append((1, current))
    return result

if __name__ == '__main__':
    sample_lists = [
        [1, 1, 2, 2, 2, 3, 4, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1],
        [],
        [7, 7, 8, 9, 9, 9, 10]
    ]
    for sample in sample_lists:
        encoded = run_length_encode(sample)
        print(encoded)