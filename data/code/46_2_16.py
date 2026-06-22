class SalaryAnalyzer:
    def __init__(self, salary_tuples):
        self.salary_tuples = salary_tuples

    def get_max_salary(self):
        if not self.salary_tuples:
            return None
        return max(salary for _, salary in self.salary_tuples)

if __name__ == '__main__':
    sample_salaries = [
        (101, 50000),
        (102, 60000),
        (103, 75000),
        (104, 55000),
        (105, 80000)
    ]
    analyzer = SalaryAnalyzer(sample_salaries)
    print(analyzer.get_max_salary())