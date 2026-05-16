class DateCalculator:
    def get_next_month(self, date_str):
        from datetime import datetime
        current_date = datetime.strptime(date_str, "%Y-%m-%d")
        if current_date.month == 12:
            next_month = current_date.replace(year=current_date.year + 1, month=1, day=1)
        else:
            next_month = current_date.replace(month=current_date.month + 1, day=1)
        return next_month.strftime("%Y-%m-%d")
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date1 = "2023-10-15"
    sample_date2 = "2023-12-31"
    sample_date3 = "2024-01-01"
    next_month1 = calculator.get_next_month(sample_date1)
    next_month2 = calculator.get_next_month(sample_date2)
    next_month3 = calculator.get_next_month(sample_date3)
    print(f"Next month after {sample_date1}: {next_month1}")
    print(f"Next month after {sample_date2}: {next_month2}")
    print(f"Next month after {sample_date3}: {next_month3}")