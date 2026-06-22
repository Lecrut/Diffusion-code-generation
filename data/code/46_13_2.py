class SalaryManager:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_highest_salary(self):
        if not self.salaries:
            return None
        highest = self.salaries[0]
        for salary in self.salaries:
            if salary > highest:
                highest = salary
        return highest

if __name__ == '__main__':
    sample_salaries = [50000, 62000, 45000, 78000, 55000]
    manager = SalaryManager(sample_salaries)
    print(manager.get_highest_salary())