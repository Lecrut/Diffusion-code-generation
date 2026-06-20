import datetime

class DateCalculator:
    @staticmethod
    def calculate_time_difference(date1: datetime.datetime, date2: datetime.datetime) -> datetime.timedelta:
        return abs(date2 - date1)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = datetime.datetime(2023, 1, 15)
    date_b = datetime.datetime(2023, 2, 20)
    result = calculator.calculate_time_difference(date_a, date_b)
    print(f"Date A: {date_a}")
    print(f"Date B: {date_b}")
    print(f"Time Difference: {result}")

    date_c = datetime.datetime(2022, 11, 20)
    result_2 = calculator.calculate_time_difference(date_a, date_c)
    print(f"Difference between Date A and Date C: {result_2}")