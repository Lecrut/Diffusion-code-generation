class SalaryAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_max_salary(self):
        if not self.data:
            return None
        max_sal = 0
        for emp_id, salary in self.data:
            if salary > max_sal:
                max_sal = salary
        return max_sal

if __name__ == '__main__':
    sample_data = [(1, 50000), (2, 62000), (3, 55000), (4, 71000)]
    analyzer = SalaryAnalyzer(sample_data)
    print(analyzer.get_max_salary())