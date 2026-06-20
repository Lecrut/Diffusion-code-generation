from datetime import date

class AgeCalculator:
    def __init__(self, birth_date):
        self.birth_date = birth_date
    
    def calculate_age(self, current_date):
        age = current_date.year - self.birth_date.year - ((current_date.month, current_date.day) < (self.birth_date.month, self.birth_date.day))
        return age

if __name__ == '__main__':
    calculator = AgeCalculator(date(1990, 3, 15))
    current_date = date(2024, 1, 1)
    age = calculator.calculate_age(current_date)
    print(age)