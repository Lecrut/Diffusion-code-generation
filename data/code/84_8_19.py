from datetime import date

class DateCalculator:
    EPOCH = date(1970, 1, 1)

    @staticmethod
    def calculate_day_of_year(input_date):
        delta = input_date - DateCalculator.EPOCH
        return delta.days + 1

if __name__ == '__main__':
    test_dates = [
        date(2023, 4, 1),
        date(2023, 12, 31),
        date(2020, 2, 29)
    ]
    
    for dt in test_dates:
        day_of_year = DateCalculator.calculate_day_of_year(dt)
        print(f"Date: {dt}, Day of Year: {day_of_year}")