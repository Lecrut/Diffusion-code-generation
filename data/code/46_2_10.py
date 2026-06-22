class SalaryAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_max_salary(self):
        if not self.data:
            return None
        max_sal = -1
        for _, salary in self.data:
            if salary > max_sal:
                max_sal = salary
        return max_sal

if __name__ == '__main__':
    sample_data = [(101, 50000), (102, 75000), (103, 62000), (104, 90000)]
    analyzer = SalaryAnalyzer(sample_data)
    result = analyzer.get_max_salary()
    print(result)