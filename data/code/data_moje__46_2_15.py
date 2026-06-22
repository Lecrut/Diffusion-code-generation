class SalaryAnalyzer:
    def __init__(self):
        self.salaries = [
            (101, 50000),
            (102, 75000),
            (103, 60000),
            (104, 95000),
            (105, 82000)
        ]

    def get_max_salary(self):
        if not self.salaries:
            return 0
        return max(salary for _, salary in self.salaries)

if __name__ == '__main__':
    analyzer = SalaryAnalyzer()
    result = analyzer.get_max_salary()
    print(result)