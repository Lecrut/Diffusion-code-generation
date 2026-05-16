class DateCalculator:
    def days_between(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        return abs((date1 - date2).days)
if __name__ == '__main__':
    import datetime
    calculator = DateCalculator()
    date1 = "2023-01-01"
    date2 = "2023-01-10"
    result = calculator.days_between(date1, date2)
    print(result)