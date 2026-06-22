class SalaryAnalyzer:
    def __init__(self, salary_data):
        self.salary_data = salary_data

    def get_max_salary(self):
        if not self.salary_data:
            return None
        max_salary = max(salary for _, salary in self.salary_data)
        return max_salary

if __name__ == '__main__':
    salary_data = [
        (101, 5000),
        (102, 7500),
        (103, 6000),
        (104, 8500),
        (105, 4000)
    ]
    analyzer = SalaryAnalyzer(salary_data)
    print(analyzer.get_max_salary())