import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    return heapq.nlargest(1, salaries)[0]

if __name__ == '__main__':
    salaries = [5000, 12000, 8000, 15000, 9000, 20000]
    result = find_largest_salary(salaries)
    print(result)