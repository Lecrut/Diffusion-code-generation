from datetime import date

class AgeCalculator:
    def __init__(self, birth_date: date, current_date: date):
        self.birth_date = birth_date
        self.current_date = current_date

    def compute(self) -> int:
        age = self.current_date.year - self.birth_date.year
        if (self.current_date.month, self.current_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def get_birth_year(self) -> int:
        return self.birth_date.year

    def get_current_year(self) -> int:
        return self.current_date.year

if __name__ == '__main__':
    birth = date(1990, 3, 15)
    today = date(2024, 1, 1)
    calculator = AgeCalculator(birth, today)
    age = calculator.compute()
    print(age)
    print(calculator.get_birth_year())
    print(calculator.get_current_year())