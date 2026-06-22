class SalaryAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_max_salary(self):
        if not self.data:
            return 0
        max_salary = self.data[0][1]
        for item in self.data:
            if item[1] > max_salary:
                max_salary = item[1]
        return max_salary

if __name__ == '__main__':
    sample_data = [
        (101, 50000),
        (102, 75000),
        (103, 62000),
        (104, 89000),
        (105, 55000)
    ]
    analyzer = SalaryAnalyzer(sample_data)
    print(analyzer.get_max_salary())