from datetime import date

class AgeCalculator:
    def __init__(self, birth_date):
        self.birth_date = birth_date
    
    def calculate_age(self):
        today = date(2024, 1, 1)
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    calculator = AgeCalculator(birth_date)
    print(calculator.calculate_age())