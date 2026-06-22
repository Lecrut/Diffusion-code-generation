import heapq

def get_max_salary(salaries):
    if not salaries:
        return None
    return -heapq.heappushpop([-s, s] for s in salaries)[1]

if __name__ == '__main__':
    sample_salaries = [4000, 15000, 7000, 25000, 9000]
    result = get_max_salary(sample_salaries)
    print(result)