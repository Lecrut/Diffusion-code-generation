class SalaryAnalyzer:
    def __init__(self, salary_data):
        self.salary_data = salary_data

    def get_max_salary(self):
        if not self.salary_data:
            return None
        return max(salary for _, salary in self.salary_data)

if __name__ == '__main__':
    sample_data = [
        (101, 50000),
        (102, 60000),
        (103, 75000),
        (104, 55000),
        (105, 80000)
    ]
    analyzer = SalaryAnalyzer(sample_data)
    print(analyzer.get_max_salary())