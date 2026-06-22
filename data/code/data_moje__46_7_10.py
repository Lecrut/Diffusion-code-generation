import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    largest = heapq.nlargest(1, salaries)
    return largest[0]

if __name__ == '__main__':
    salaries = [50000, 120000, 95000, 30000, 150000, 80000, 45000]
    result = find_largest_salary(salaries)
    print(result)