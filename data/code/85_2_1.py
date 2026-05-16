from datetime import date
class DateCalculator:
    def difference_in_weeks(self, date1, date2):
        time_difference = abs(date1 - date2)
        difference_in_weeks = time_difference.days / 7
        return int(round(difference_in_weeks))
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 29)
    date_c = date(2024, 1, 1)
    date_d = date(2024, 1, 1)
    date_e = date(2023, 10, 10)
    date_f = date(2023, 10, 20)
    print(f"Difference between {date_a} and {date_b}: {calculator.difference_in_weeks(date_a, date_b)} weeks")
    print(f"Difference between {date_c} and {date_d}: {calculator.difference_in_weeks(date_c, date_d)} weeks")
    print(f"Difference between {date_e} and {date_f}: {calculator.difference_in_weeks(date_e, date_f)} weeks")