class DateCalculator:
    def get_next_month(self, date_str):
        from datetime import datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj.month == 12:
            next_month = date_obj.replace(year=date_obj.year + 1, month=1, day=1)
        else:
            next_month = date_obj.replace(month=date_obj.month + 1, day=date_obj.day)
        return next_month.strftime("%Y-%m-%d")
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = "2023-10-15"
    next_date = calculator.get_next_month(sample_date)
    print(f"The next month after {sample_date} is {next_date}")
    sample_date_dec = "2023-12-01"
    next_date_dec = calculator.get_next_month(sample_date_dec)
    print(f"The next month after {sample_date_dec} is {next_date_dec}")