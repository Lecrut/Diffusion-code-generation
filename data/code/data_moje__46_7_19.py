import heapq

def find_largest_salary(salaries: list[int]) -> int:
    return -heapq.nsmallest(1, [-s for s in salaries])[0]

if __name__ == '__main__':
    salaries = [5000, 12000, 8500, 3000, 20000, 15000, 9500]
    result = find_largest_salary(salaries)
    print(result)