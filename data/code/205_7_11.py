import heapq

def heapify_and_sort(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")
    
    min_heap = []
    for number in numbers:
        heapq.heappush(min_heap, number)
    
    return [heapq.heappop(min_heap) for _ in range(len(numbers))]

if __name__ == '__main__':
    sample_values = [5, 3, 8, 4, 2]
    sorted_values = heapify_and_sort(sample_values)
    print(sorted_values)