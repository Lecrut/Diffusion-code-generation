class SalaryManager:
    def __init__(self):
        self.salaries = [45000, 52000, 68000, 75000, 49000, 82000, 61000]

    def get_highest_salary(self):
        if not self.salaries:
            return None
        return max(self.salaries)

if __name__ == '__main__':
    manager = SalaryManager()
    highest = manager.get_highest_salary()
    print(highest)