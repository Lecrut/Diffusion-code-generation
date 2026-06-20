class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def get_next_month(date_str):
        from datetime import datetime, timedelta
        date_obj = datetime.strptime(date_str, DateCalculator.DATE_FORMAT)
        next_month = (date_obj + timedelta(days=31)).replace(day=1)
        return next_month.strftime(DateCalculator.DATE_FORMAT)

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