class SalaryManager:
    def __init__(self):
        self._salaries = [45000, 62000, 51000, 78000, 49000, 65000, 55000]

    def get_highest_salary(self):
        return max(self._salaries)

if __name__ == '__main__':
    manager = SalaryManager()
    print(manager.get_highest_salary())