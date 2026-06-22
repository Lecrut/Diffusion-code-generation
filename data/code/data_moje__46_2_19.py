class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_max_salary(self):
        if not self.salaries:
            return 0
        return max(salary for _, salary in self.salaries)

if __name__ == '__main__':
    data = [(101, 50000), (102, 75000), (103, 60000)]
    analyzer = SalaryAnalyzer(data)
    print(analyzer.get_max_salary())