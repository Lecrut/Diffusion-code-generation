class SalaryManager:
    def __init__(self, salaries=None):
        if salaries is None:
            self.salaries = []
        else:
            self.salaries = list(salaries)

    def add_salary(self, salary):
        self.salaries.append(salary)

    def get_highest_salary(self):
        if not self.salaries:
            return None
        highest = self.salaries[0]
        for salary in self.salaries[1:]:
            if salary > highest:
                highest = salary
        return highest

if __name__ == '__main__':
    manager = SalaryManager([50000, 60000, 75000, 55000, 80000])
    highest = manager.get_highest_salary()
    print(highest)