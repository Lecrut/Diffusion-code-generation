import statistics

def extract_median(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2
    else:
        return sorted_seq[mid]

if __name__ == '__main__':
    odd_sequence = [3, 1, 4, 1, 5, 9, 2]
    even_sequence = [3, 1, 4, 1, 5, 9]
    print(extract_median(odd_sequence))
    print(extract_median(even_sequence))