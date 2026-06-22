import heapq

class SalaryAnalyzer:
    def __init__(self, salary_list):
        self.salary_list = salary_list

    def get_max_salary(self):
        if not self.salary_list:
            return None
        heap_size = 1
        return heapq.nlargest(heap_size, self.salary_list)[0]

if __name__ == '__main__':
    data = [12000, 45000, 8900, 150000, 33000, 67000, 9900, 21000]
    analyzer = SalaryAnalyzer(data)
    max_val = analyzer.get_max_salary()
    print(max_val)