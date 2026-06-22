class SalaryManager:
    def __init__(self, salaries=None):
        if salaries is None:
            self.salaries = []
        else:
            self.salaries = list(salaries)

    def get_highest_salary(self):
        if not self.salaries:
            return None
        return max(self.salaries)

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 95000, 42000, 110000]
    manager = SalaryManager(sample_salaries)
    highest = manager.get_highest_salary()
    print(highest)