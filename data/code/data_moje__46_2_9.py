class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salary_data = salaries

    def get_max_salary(self):
        if not self.salary_data:
            return None
        max_salary = 0
        for _, salary in self.salary_data:
            if salary > max_salary:
                max_salary = salary
        return max_salary

if __name__ == '__main__':
    sample_salaries = [(101, 50000), (102, 65000), (103, 55000), (104, 82000)]
    analyzer = SalaryAnalyzer(sample_salaries)
    print(analyzer.get_max_salary())