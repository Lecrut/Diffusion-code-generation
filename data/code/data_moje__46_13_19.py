class SalaryManager:
    def __init__(self):
        self.salaries = [50000, 75000, 120000, 95000, 60000, 150000, 85000]

    def get_highest_salary(self):
        if not self.salaries:
            return 0
        highest = self.salaries[0]
        for salary in self.salaries[1:]:
            if salary > highest:
                highest = salary
        return highest

if __name__ == '__main__':
    manager = SalaryManager()
    print(manager.get_highest_salary())