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
        return find_median_efficient(data)
    else:
        k1 = n // 2 - 1
        k2 = n // 2
        import heapq
        return find_median_efficient(data)
if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(500000)]
    print("Finding median using standard sort (most practical exact method):")
    median_result = find_median_efficient(large_dataset)
    print(f"Median: {median_result}")
    odd_dataset = [1, 5, 2, 8, 3]
    print("\nTest Case (Odd Length):")
    median_odd = find_median_efficient(odd_dataset)
    print(f"Data: {odd_dataset}")
    print(f"Median: {median_odd}")
    even_dataset = [10, 20, 5, 30]
    print("\nTest Case (Even Length):")
    median_even = find_median_efficient(even_dataset)
    print(f"Data: {even_dataset}")
    print(f"Median: {median_even}")