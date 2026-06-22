class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_max_salary(self):
        if not self.salaries:
            return None
        max_salary = max(salary for _, salary in self.salaries)
        return max_salary

if __name__ == '__main__':
    sample_salaries = [
        (1, 50000),
        (2, 60000),
        (3, 75000),
        (4, 55000),
        (5, 80000)
    ]
    analyzer = SalaryAnalyzer(sample_salaries)
    print(analyzer.get_max_salary())