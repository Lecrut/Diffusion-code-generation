def find_median(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError("Sequence is empty")
    
    sorted_sequence = sequence.copy()
    for i in range(n):
        for j in range(i + 1, n):
            if sorted_sequence[i] > sorted_sequence[j]:
                sorted_sequence[i], sorted_sequence[j] = sorted_sequence[j], sorted_sequence[i]
    
    middle_index = n // 2
    if n % 2 == 1:
        return sorted_sequence[middle_index]
    else:
        return (sorted_sequence[middle_index - 1] + sorted_sequence[middle_index]) / 2

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    result = find_median(sample_sequence)
    print(result)