import heapq

def find_largest_salary(salaries):
    k = 1
    heap = []
    for salary in salaries:
        if len(heap) < k:
            heapq.heappush(heap, salary)
        else:
            if salary > heap[0]:
                heapq.heapreplace(heap, salary)
    return heap[0]

if __name__ == '__main__':
    sample_salaries = [50000, 60000, 75000, 45000, 82000, 55000, 90000, 70000]
    result = find_largest_salary(sample_salaries)
    print(result)