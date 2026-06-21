import heapq

def get_median_element(sequence):
    if not sequence:
        return None
    if len(sequence) % 2 == 1:
        index = len(sequence) // 2
        return sorted(sequence)[index]
    sorted_seq = sorted(sequence)
    lower_mid = sorted_seq[len(sequence) // 2 - 1]
    upper_mid = sorted_seq[len(sequence) // 2]
    return (lower_mid + upper_mid) / 2

if __name__ == '__main__':
    sample_odd = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sample_even = [3, 1, 4, 1, 5, 9, 2, 6]
    result_odd = get_median_element(sample_odd)
    result_even = get_median_element(sample_even)
    print(f"Median of odd sequence: {result_odd}")
    print(f"Median of even sequence: {result_even}")