class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        return abs((date2 - date1).days)
if __name__ == '__main__':
    import datetime
    calculator = DateCalculator()
    date_a = "2023-01-01"
    date_b = "2023-01-10"
    difference = calculator.calculate_difference(date_a, date_b)
    print(difference)