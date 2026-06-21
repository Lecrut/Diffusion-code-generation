import heapq

def heapify_sort(numbers):
    min_heap = numbers[:]
    heapq.heapify(min_heap)
    sorted_numbers = []
    while min_heap:
        sorted_numbers.append(heapq.heappop(min_heap))
    return sorted_numbers

if __name__ == '__main__':
    sample_values = [9, 1, 7, 3, 8, 2]
    sorted_values = heapify_sort(sample_values)
    print(sorted_values)