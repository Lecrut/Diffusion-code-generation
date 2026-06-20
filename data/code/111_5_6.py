import datetime

class AgeCalculator:
    BIRTH_DATE = datetime.date(1990, 3, 15)
    
    @staticmethod
    def calculate_age(birth_date):
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    
if __name__ == '__main__':
    calculator = AgeCalculator()
    age = calculator.calculate_age(AgeCalculator.BIRTH_DATE)
    print(age)