from datetime import datetime
class DateCalculator:
    def get_week_diff(self, date1, date2):
        time_difference = abs(date1 - date2)
        weeks = time_difference.days / 7.0
        return weeks
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 15)
    date_c = datetime(2023, 1, 1)
    date_d = datetime(2023, 1, 2)
    diff1 = calculator.get_week_diff(date_a, date_b)
    diff2 = calculator.get_week_diff(date_c, date_d)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {diff1} weeks")
    print(f"Difference between {date_c.date()} and {date_d.date()}: {diff2} weeks")