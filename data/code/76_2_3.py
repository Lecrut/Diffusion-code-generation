class DateCalculator:
    def days_between(self, date1_str, date2_str):
        from datetime import datetime
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        return abs((date2 - date1).days)
if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = "2023-01-01"
    date_b = "2023-01-10"
    result1 = calculator.days_between(date_a, date_b)
    print(result1)
    date_c = "2024-12-31"
    date_d = "2024-01-01"
    result2 = calculator.days_between(date_c, date_d)
    print(result2)