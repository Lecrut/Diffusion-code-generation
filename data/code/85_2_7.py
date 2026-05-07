from datetime import date
class DateCalculator:
    def difference_in_weeks(self, date1, date2):
        time_difference = abs(date1 - date2)
        weeks = time_difference.days / 7
        return int(weeks)
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 22)
    date_c = date(2022, 12, 31)
    date_d = date(2024, 1, 1)
    diff1 = calculator.difference_in_weeks(date_a, date_b)
    diff2 = calculator.difference_in_weeks(date_c, date_d)
    diff3 = calculator.difference_in_weeks(date_a, date_c)
    diff4 = calculator.difference_in_weeks(date_d, date_a)
    print(f"Difference between {date_a} and {date_b}: {diff1} weeks")
    print(f"Difference between {date_c} and {date_d}: {diff2} weeks")
    print(f"Difference between {date_a} and {date_c}: {diff3} weeks")
    print(f"Difference between {date_d} and {date_a}: {diff4} weeks")