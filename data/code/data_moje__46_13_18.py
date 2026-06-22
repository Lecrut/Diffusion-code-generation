class SalaryManager:
    def __init__(self):
        self.salaries = [55000, 72000, 48000, 91000, 63000]

    def get_highest_salary(self):
        return max(self.salaries)

if __name__ == '__main__':
    manager = SalaryManager()
    print(manager.get_highest_salary())