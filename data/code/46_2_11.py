class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_max_salary(self):
        if not self.salaries:
            return None
        max_salary = self.salaries[0][1]
        for _, salary in self.salaries[1:]:
            if salary > max_salary:
                max_salary = salary
        return max_salary

if __name__ == '__main__':
    sample_salaries = [(101, 50000), (102, 75000), (103, 62000), (104, 91000), (105, 55000)]
    analyzer = SalaryAnalyzer(sample_salaries)
    result = analyzer.get_max_salary()
    print(result)