class SalaryAnalyzer:
    def __init__(self, salary_data):
        self.salary_data = salary_data

    def get_max_salary(self):
        if not self.salary_data:
            return 0
        return max(salary for _, salary in self.salary_data)

if __name__ == '__main__':
    sample_salary_data = [
        (101, 75000),
        (102, 85000),
        (103, 65000),
        (104, 95000),
        (105, 80000)
    ]
    analyzer = SalaryAnalyzer(sample_salary_data)
    print(analyzer.get_max_salary())