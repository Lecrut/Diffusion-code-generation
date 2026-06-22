class SalaryAnalyzer:
    def __init__(self):
        self.salaries = [
            (101, 50000),
            (102, 75000),
            (103, 60000),
            (104, 95000),
            (105, 45000),
            (106, 82000),
            (107, 55000),
            (108, 70000),
            (109, 65000),
            (110, 88000),
        ]

    def get_max_salary(self):
        max_salary = self.salaries[0][1]
        for record in self.salaries:
            if record[1] > max_salary:
                max_salary = record[1]
        return max_salary

if __name__ == '__main__':
    analyzer = SalaryAnalyzer()
    result = analyzer.get_max_salary()
    print(result)