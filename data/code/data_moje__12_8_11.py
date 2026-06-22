import heapq

def find_median(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    
    n = len(sequence)
    sorted_seq = sorted(sequence)
    
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_seq[mid - 1] + sorted_seq[mid]) / 2.0
    else:
        median = sorted_seq[mid]
    
    return median

if __name__ == '__main__':
    samples = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_median(samples)
    print(result)