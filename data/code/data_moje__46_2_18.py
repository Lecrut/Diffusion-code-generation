class SalaryAnalyzer:
    def __init__(self, salary_tuples):
        self.salary_tuples = salary_tuples

    def get_max_salary(self):
        if not self.salary_tuples:
            return None
        max_salary = self.salary_tuples[0][1]
        for employee_id, salary in self.salary_tuples:
            if salary > max_salary:
                max_salary = salary
        return max_salary

if __name__ == '__main__':
    data = [(1, 50000), (2, 60000), (3, 55000), (4, 70000)]
    analyzer = SalaryAnalyzer(data)
    print(analyzer.get_max_salary())