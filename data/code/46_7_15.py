import heapq

def find_top_salary(salaries):
    if not salaries:
        return None
    k = 1
    heap = []
    for salary in salaries:
        if len(heap) < k:
            heapq.heappush(heap, salary)
        else:
            heapq.heappushpop(heap, salary)
    return heapq.nsmallest(k, heap)[-1]

if __name__ == '__main__':
    hardcoded_salaries = [45000, 62000, 78000, 55000, 91000, 48000, 85000, 70000, 99000, 60000]
    max_sal = find_top_salary(hardcoded_salaries)
    print(max_sal)