from datetime import datetime
class DateCalculator:
    def get_week_diff(self, date1, date2):
        time_difference = abs(date1 - date2)
        weeks = time_difference.days / 7
        return weeks
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 15)
    date_c = datetime(2023, 6, 1)
    date_d = datetime(2023, 6, 20)
    diff_ab = calculator.get_week_diff(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {diff_ab:.2f} weeks")
    diff_cd = calculator.get_week_diff(date_c, date_d)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {diff_cd:.2f} weeks")
    diff_ac = calculator.get_week_diff(date_a, date_c)
    print(f"Difference between {date_a.date()} and {date_c.date()}: {diff_ac:.2f} weeks")