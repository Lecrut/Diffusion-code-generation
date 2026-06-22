class SalaryAnalyzer:
    def __init__(self, salary_data):
        self.salary_data = salary_data

    def get_max_salary(self):
        if not self.salary_data:
            return 0
        max_salary = self.salary_data[0][1]
        for record in self.salary_data:
            if record[1] > max_salary:
                max_salary = record[1]
        return max_salary

if __name__ == '__main__':
    data = [(101, 50000), (102, 75000), (103, 65000), (104, 90000)]
    analyzer = SalaryAnalyzer(data)
    result = analyzer.get_max_salary()
    print(result)