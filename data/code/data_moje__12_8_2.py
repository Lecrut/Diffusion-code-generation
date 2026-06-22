import heapq

def get_median_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    n = len(sequence)
    if n % 2 == 1:
        return heapq.nsmallest(n // 2 + 1, sequence)[-1]
    else:
        left_mid = heapq.nsmallest(n // 2, sequence)[-1]
        right_mid = heapq.nsmallest(n // 2 + 1, sequence)[n // 2]
        return (left_mid + right_mid) / 2

if __name__ == '__main__':
    sample_odd = [7, 2, 9, 1, 5, 3, 8]
    sample_even = [10, 4, 6, 2, 8, 0]
    result_odd = get_median_element(sample_odd)
    result_even = get_median_element(sample_even)
    print(result_odd)
    print(result_even)