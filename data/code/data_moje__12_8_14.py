import heapq

def get_median(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_seq[mid]
    else:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2

def find_median_heap(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    
    lower_half = []
    upper_half = []
    
    for num in sequence:
        if not lower_half or num <= -lower_half[0]:
            heapq.heappush(lower_half, -num)
        else:
            heapq.heappush(upper_half, num)
        
        if len(lower_half) > len(upper_half) + 1:
            heapq.heappush(upper_half, -heapq.heappop(lower_half))
        elif len(upper_half) > len(lower_half):
            heapq.heappush(lower_half, -heapq.heappop(upper_half))
    
    if len(sequence) % 2 == 1:
        return -lower_half[0]
    else:
        return (-lower_half[0] + upper_half[0]) / 2

if __name__ == '__main__':
    data_odd = [15, 3, 9, 27, 5]
    data_even = [10, 2, 8, 4, 6, 12]
    
    print(get_median(data_odd))
    print(get_median(data_even))
    print(find_median_heap(data_odd))
    print(find_median_heap(data_even))