from datetime import date
class DateCalculator:
    def difference_in_weeks(self, date1, date2):
        time_difference = abs(date1 - date2)
        weeks = time_difference.days / 7
        return int(weeks)
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 29)
    date_c = date(2023, 7, 1)
    date_d = date(2024, 1, 1)
    diff_ab = calculator.difference_in_weeks(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {diff_ab} weeks")
    diff_cd = calculator.difference_in_weeks(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {diff_cd} weeks")
    diff_ac = calculator.difference_in_weeks(date_a, date_c)
    print(f"Difference between {date_a} and {date_c}: {diff_ac} weeks")