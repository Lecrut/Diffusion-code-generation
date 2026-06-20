from datetime import datetime, timedelta

class DateHandler:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def get_next_month(date_str):
        current_date = datetime.strptime(date_str, DateHandler.DATE_FORMAT)
        next_month = current_date + timedelta(days=31)
        return next_month.strftime(DateHandler.DATE_FORMAT)

if __name__ == '__main__':
    handler = DateHandler()
    sample_date1 = "2023-10-15"
    sample_date2 = "2023-12-31"
    sample_date3 = "2024-01-01"
    next_month1 = handler.get_next_month(sample_date1)
    next_month2 = handler.get_next_month(sample_date2)
    next_month3 = handler.get_next_month(sample_date3)
    print(f"Next month after {sample_date1}: {next_month1}")
    print(f"Next month after {sample_date2}: {next_month2}")
    print(f"Next month after {sample_date3}: {next_month3}")