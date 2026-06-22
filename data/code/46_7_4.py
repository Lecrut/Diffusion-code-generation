import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    return -heapq.heappushpop([-salaries[0]], -salaries[0]) if len(salaries) > 1 else salaries[0]

if __name__ == '__main__':
    salaries = [5000, 12000, 7500, 9000, 3000, 15000, 8000]
    result = find_largest_salary(salaries)
    print(result)