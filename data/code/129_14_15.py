import heapq

def filter_and_sort(items, k, threshold):
    if not isinstance(items, list) or not all(isinstance(item, tuple) and len(item) == 2 for item in items):
        raise ValueError("items must be a list of tuples with exactly two elements")
    
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")
    
    if not isinstance(threshold, (int, float)):
        raise ValueError("threshold must be a number")
    
    filtered_items = [item for item in items if item[1] > threshold]
    return heapq.nlargest(k, filtered_items, key=lambda x: x[1])

if __name__ == '__main__':
    data = [(3, 1), (1, 5), (4, 2), (2, 8)]
    k = 2
    threshold = 5
    result = filter_and_sort(data, k, threshold)
    print(result)