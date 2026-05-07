from datetime import date
class DateCalculator:
    def difference_in_weeks(self, date1, date2):
        time_difference = abs(date1 - date2)
        return time_difference.days / 7
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 29)
    date_c = date(2023, 1, 1)
    date_d = date(2023, 2, 1)
    diff_ab = calculator.difference_in_weeks(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {diff_ab} weeks")
    diff_ac = calculator.difference_in_weeks(date_a, date_c)
    print(f"Difference between {date_a} and {date_c}: {diff_ac} weeks")
    diff_ad = calculator.difference_in_weeks(date_a, date_d)
    print(f"Difference between {date_a} and {date_d}: {diff_ad} weeks")