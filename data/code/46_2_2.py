class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salary_list = salaries

    def get_max_salary(self):
        if not self.salary_list:
            return None
        max_salary = self.salary_list[0][1]
        for employee_id, salary in self.salary_list[1:]:
            if salary > max_salary:
                max_salary = salary
        return max_salary

if __name__ == '__main__':
    sample_data = [(101, 50000), (102, 75000), (103, 62000), (104, 88000)]
    analyzer = SalaryAnalyzer(sample_data)
    print(analyzer.get_max_salary())