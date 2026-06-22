import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    return heapq.nlargest(1, salaries)[0]

if __name__ == '__main__':
    sample_salaries = [50000, 60000, 45000, 75000, 55000, 80000, 40000, 90000]
    result = find_largest_salary(sample_salaries)
    print(result)