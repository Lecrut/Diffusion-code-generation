import heapq

def validate_input(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numbers")

def heap_sort(numbers):
    validate_input(numbers)
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