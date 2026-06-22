import heapq

def find_largest_salary(salaries):
    if not salaries:
        raise ValueError("Salary list cannot be empty")
    
    return -heapq.nlargest(1, [-s for s in salaries])[0]

if __name__ == '__main__':
    salaries = [50000, 120000, 75000, 90000, 200000, 60000]
    
    largest = find_largest_salary(salaries)
    
    print(largest)