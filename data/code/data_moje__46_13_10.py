class SalaryManager:
    def __init__(self):
        self.salary_data = [50000, 60000, 75000, 80000, 90000, 95000, 110000]

    def get_highest_salary(self):
        highest = self.salary_data[0]
        for salary in self.salary_data:
            if salary > highest:
                highest = salary
        return highest

if __name__ == '__main__':
    manager = SalaryManager()
    highest_salary = manager.get_highest_salary()
    print(highest_salary)