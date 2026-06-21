import heapq

def heap_sort(numbers):
    heapq.heapify(numbers)
    sorted_numbers = [heapq.heappop(numbers) for _ in range(len(numbers))]
    return sorted_numbers

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(heap_sort(sample_values))