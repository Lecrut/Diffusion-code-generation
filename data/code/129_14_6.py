import heapq

def conditional_sort(data, k, threshold):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("All items must be tuples of length 2")
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")
    if not isinstance(threshold, (int, float)):
        raise ValueError("Threshold must be a number")

    filtered_data = [item for item in data if item[1] > threshold]
    return heapq.nlargest(k, filtered_data, key=lambda x: x[1])

if __name__ == '__main__':
    data = [(3, 1), (1, 0), (4, 2), (2, 3)]
    k = 2
    threshold = 1
    result = conditional_sort(data, k, threshold)
    print(result)