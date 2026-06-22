import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    largest_k = 1
    top_k = heapq.nlargest(largest_k, salaries)
    return top_k[0]

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 30000, 90000, 45000, 85000, 60000]
    result = find_largest_salary(sample_salaries)
    print(result)