import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    largest_value = heapq.nlargest(1, salaries)
    return largest_value[0]

if __name__ == '__main__':
    sample_salaries = [50000, 60000, 45000, 90000, 30000, 85000, 72000, 95000, 40000, 55000]
    result = find_largest_salary(sample_salaries)
    print(result)