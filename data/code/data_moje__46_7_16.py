import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    if len(salaries) == 1:
        return salaries[0]
    largest_elements = heapq.nlargest(1, salaries)
    return largest_elements[0]

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 120000, 85000, 95000, 200000, 30000, 150000]
    result = find_largest_salary(sample_salaries)
    print(result)