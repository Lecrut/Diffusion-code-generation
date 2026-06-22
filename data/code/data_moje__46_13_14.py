class SalaryManager:
    def __init__(self, salaries):
        self.salaries = salaries

    def get_highest_salary(self):
        if not self.salaries:
            return None
        highest = self.salaries[0]
        for salary in self.salaries[1:]:
            if salary > highest:
                highest = salary
        return highest

if __name__ == '__main__':
    sample_salaries = [45000, 62000, 55000, 78000, 51000]
    manager = SalaryManager(sample_salaries)
    print(manager.get_highest_salary())