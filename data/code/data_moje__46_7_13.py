import heapq

def find_largest_salary(salaries, k=1):
    if not salaries:
        return None
    heap = []
    for salary in salaries:
        heapq.heappush(heap, salary)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
if __name__ == '__main__':
    hardcoded_salaries = [55000, 72000, 48000, 95000, 63000, 88000, 41000, 77000, 59000, 91000]
    largest = find_largest_salary(hardcoded_salaries, k=1)
    print(largest)