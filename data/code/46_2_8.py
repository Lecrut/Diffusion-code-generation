class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_max_salary(self):
        if not self.salaries:
            return None
        max_salary = 0
        for employee_id, salary in self.salaries:
            if salary > max_salary:
                max_salary = salary
        return max_salary

if __name__ == '__main__':
    sample_data = [(101, 50000), (102, 75000), (103, 62000), (104, 91000)]
    analyzer = SalaryAnalyzer(sample_data)
    print(analyzer.get_max_salary())