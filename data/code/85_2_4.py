from datetime import date
class DateCalculator:
    def difference_in_weeks(self, date1, date2):
        time_difference = abs(date1 - date2)
        difference_in_weeks = time_difference.days / 7
        return int(difference_in_weeks)
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 29)
    date_c = date(2022, 12, 31)
    date_d = date(2023, 7, 1)
    diff1 = calculator.difference_in_weeks(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {diff1} weeks")
    diff2 = calculator.difference_in_weeks(date_c, date_a)
    print(f"Difference between {date_c} and {date_a}: {diff2} weeks")
    diff3 = calculator.difference_in_weeks(date_d, date_a)
    print(f"Difference between {date_d} and {date_a}: {diff3} weeks")