import heapq

def find_largest_salary(salaries):
    n = len(salaries)
    k = 1
    if k >= n:
        return max(salaries)
    heap = []
    for salary in salaries:
        if len(heap) < k:
            heapq.heappush(heap, salary)
        else:
            if salary > heap[0]:
                heapq.heapreplace(heap, salary)
    return max(heap)

if __name__ == '__main__':
    sample_salaries = [5000, 12000, 8500, 15000, 9500, 20000, 11000, 7000, 18000, 6000]
    result = find_largest_salary(sample_salaries)
    print(result)