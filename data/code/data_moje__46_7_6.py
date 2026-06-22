import heapq

def find_largest_salary(salaries):
    if not salaries:
        return None
    top_one = heapq.nlargest(1, salaries)
    return top_one[0]

if __name__ == '__main__':
    sample_salaries = [45000, 52000, 61000, 78000, 33000, 95000, 21000, 88000]
    result = find_largest_salary(sample_salaries)
    print(result)