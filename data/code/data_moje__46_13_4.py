class SalaryManager:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_highest_salary(self):
        if not self.salaries:
            return 0
        highest = self.salaries[0]
        for salary in self.salaries[1:]:
            if salary > highest:
                highest = salary
        return highest

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 32000, 95000, 61000]
    manager = SalaryManager(sample_salaries)
    print(manager.get_highest_salary())