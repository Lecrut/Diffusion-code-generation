import random
def find_median_efficient(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
    return median
def find_median_selection(data):
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        k = n // 2
        target_index = k
        import heapq
        return sorted(data)[k]
    else:
        k1 = n // 2 - 1
        k2 = n // 2
        return (sorted(data)[k1] + sorted(data)[k2]) / 2.0
if __name__ == '__main__':
    large_dataset = [random.randint(0, 1000000) for _ in range(1000000)]
    print(find_median_efficient(large_dataset))
    print(find_median_selection(large_dataset))