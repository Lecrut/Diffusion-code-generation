import heapq

def find_largest_salary(salaries):
    k = 1
    if not salaries:
        return None
    min_heap = []
    for salary in salaries:
        if len(min_heap) < k:
            heapq.heappush(min_heap, salary)
        elif salary > min_heap[0]:
            heapq.heapreplace(min_heap, salary)
    return min_heap[0]
if __name__ == '__main__':
    hardcoded_salaries = [72000, 85000, 95000, 62000, 110000, 78000, 99000, 55000, 105000, 88000]
    result = find_largest_salary(hardcoded_salaries)
    print(result)