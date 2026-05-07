class DateCalculator:
    def get_week_diff(self, date1, date2):
        time_difference = abs(date1 - date2)
        weeks = time_difference.days / 7
        return weeks
if __name__ == '__main__':
    from datetime import datetime
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 15)
    calculator = DateCalculator()
    diff1 = calculator.get_week_diff(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {diff1} weeks")
    date_c = datetime(2023, 1, 1)
    date_d = datetime(2023, 1, 29)
    diff2 = calculator.get_week_diff(date_c, date_d)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {diff2} weeks")
    date_e = datetime(2023, 1, 1)
    date_f = datetime(2022, 1, 1)
    diff3 = calculator.get_week_diff(date_e, date_f)
    print(f"Difference between {date_e.date()} and {date_f.date()}: {diff3} weeks")