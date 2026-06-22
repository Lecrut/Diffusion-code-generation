class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salary_data = salaries

    def get_max_salary(self):
        if not self.salary_data:
            return None
        max_salary = self.salary_data[0][1]
        for _, salary in self.salary_data:
            if salary > max_salary:
                max_salary = salary
        return max_salary

if __name__ == '__main__':
    sample_salaries = [(101, 50000), (102, 75000), (103, 62000), (104, 85000), (105, 55000)]
    analyzer = SalaryAnalyzer(sample_salaries)
    result = analyzer.get_max_salary()
    print(result)