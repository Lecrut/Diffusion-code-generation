import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    if len(salaries) == 1:
        return salaries[0]
    k = 1
    largest_k_heap = []
    for salary in salaries:
        if len(largest_k_heap) < k:
            heapq.heappush(largest_k_heap, salary)
        elif salary > largest_k_heap[0]:
            heapq.heapreplace(largest_k_heap, salary)
    return largest_k_heap[0]

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 120000, 65000, 90000, 45000, 110000, 85000]
    result = find_largest_salary(sample_salaries)
    print(result)