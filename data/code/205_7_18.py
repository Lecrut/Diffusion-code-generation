import heapq

def heap_sort(numbers):
    heapq.heapify(numbers)
    return [heapq.heappop(numbers) for _ in range(len(numbers))]

if __name__ == '__main__':
    sample_values = [9, 3, 7, 1, 2]
    sorted_values = heap_sort(sample_values)
    print(sorted_values)