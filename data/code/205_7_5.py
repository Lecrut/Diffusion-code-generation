import heapq

def heap_sort(numbers):
    heapq.heapify(numbers)
    return [heapq.heappop(numbers) for _ in range(len(numbers))]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_values = heap_sort(sample_values)
    print(sorted_values)