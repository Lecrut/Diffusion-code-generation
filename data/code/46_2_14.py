class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salary_list = salaries

    def get_max_salary(self):
        if not self.salary_list:
            return None
        max_val = 0
        for _, salary in self.salary_list:
            if salary > max_val:
                max_val = salary
        return max_val

if __name__ == '__main__':
    sample_data = [(101, 50000), (102, 75000), (103, 62000), (104, 90000), (105, 45000)]
    analyzer = SalaryAnalyzer(sample_data)
    result = analyzer.get_max_salary()
    print(result)