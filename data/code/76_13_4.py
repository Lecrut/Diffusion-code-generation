import datetime
class DateCalculator:
    def get_difference(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        return abs((date2 - date1).days)
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = "2023-01-01"
    date_b = "2023-01-10"
    difference1 = calculator.get_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {difference1} days")
    date_c = "2024-12-31"
    date_d = "2024-01-01"
    difference2 = calculator.get_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {difference2} days")