class SalaryManager:
    def __init__(self):
        self.salaries = [50000, 75000, 90000, 120000, 65000, 85000]

    def get_highest_salary(self):
        return max(self.salaries)

if __name__ == '__main__':
    manager = SalaryManager()
    print(manager.get_highest_salary())