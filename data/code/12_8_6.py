import heapq

def get_median(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    n = len(sequence)
    sorted_seq = sorted(sequence)
    mid = n // 2
    if n % 2 == 1:
        return sorted_seq[mid]
    return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2

if __name__ == '__main__':
    data_sets = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [10, 20, 30, 40],
        [1, 2, 3],
        [5]
    ]
    for data in data_sets:
        print(f"Data: {data}, Median: {get_median(data)}")