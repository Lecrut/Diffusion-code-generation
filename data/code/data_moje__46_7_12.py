import heapq

def find_largest_salary(salaries, k=1):
    if k <= 0:
        return None
    if not salaries:
        return None
    
    min_heap = []
    for salary in salaries:
        if len(min_heap) < k:
            heapq.heappush(min_heap, salary)
        else:
            if salary > min_heap[0]:
                heapq.heapreplace(min_heap, salary)
    
    return min_heap[0] if min_heap else None

if __name__ == '__main__':
    salaries = [45000, 120000, 89000, 150000, 72000, 95000, 110000, 60000, 135000, 55000]
    largest = find_largest_salary(salaries, k=1)
    print(largest)