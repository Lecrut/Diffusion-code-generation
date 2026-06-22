from datetime import date, timedelta

class AgeCalculator:
    def __init__(self, birth_year, birth_month, birth_day):
        self.birth_date = date(birth_year, birth_month, birth_day)

    def calculate_age(self, current_date):
        age = current_date.year - self.birth_date.year
        if current_date.month < self.birth_date.month:
            age -= 1
        elif current_date.month == self.birth_date.month and current_date.day < self.birth_date.day:
            age -= 1
        return age

    def get_birth_date(self):
        return self.birth_date

    def get_current_date(self):
        return self.birth_date

if __name__ == '__main__':
    calculator = AgeCalculator(1990, 3, 15)
    current_date = date(2024, 1, 1)
    age = calculator.calculate_age(current_date)
    print(age)
    print(calculator.get_birth_date())
    print(calculator.get_current_date())