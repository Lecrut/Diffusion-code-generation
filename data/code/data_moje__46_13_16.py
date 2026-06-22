class SalaryManager:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_highest_salary(self):
        if not self.salaries:
            return None
        return max(self.salaries)

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 62000, 98000, 55000]
    manager = SalaryManager(sample_salaries)
    print(manager.get_highest_salary())