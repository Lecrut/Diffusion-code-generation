def find_median(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    sorted_sequence = sorted(sequence)
    n = len(sorted_sequence)
    mid = n // 2
    if n % 2 == 1:
        return sorted_sequence[mid]
    else:
        return (sorted_sequence[mid - 1] + sorted_sequence[mid]) / 2

if __name__ == '__main__':
    data_sets = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [10, 20, 30, 40, 50],
        [7, 7, 7, 7],
        [5, 1, 8, 3, 2, 9, 4]
    ]
    for data in data_sets:
        result = find_median(data)
        print(f"Input: {data} -> Median: {result}")