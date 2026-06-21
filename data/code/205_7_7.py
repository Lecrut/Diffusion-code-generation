import heapq

def heap_sort(numbers):
    min_heap = []
    for number in numbers:
        heapq.heappush(min_heap, number)
    sorted_numbers = []
    while min_heap:
        sorted_numbers.append(heapq.heappop(min_heap))
    return sorted_numbers

if __name__ == '__main__':
    sample_values = [4, 1, 7, 3, 2, 5]
    sorted_values = heap_sort(sample_values)
    print(sorted_values)