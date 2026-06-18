import datetime
class DateMonthCalculator:
    def add_months(self, date_str: str, months: int) -> str:
        if not isinstance(date_str, str):
            raise TypeError("Date string must be provided.")
        try:
            parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD'. Error: {e}") from e
        if not isinstance(months, int) or months < 0:
            raise TypeError("Months must be a non-negative integer.")
        try:
            new_date = parsed_date + datetime.timedelta(days=31 * months)
            year = new_date.year
            month = new_date.month
            while True:
                if not isinstance(month, int):
                    break
                days_in_month = calendar_days(year, month)
                day_of_year = date_to_day_of_year(new_date)
                remaining_months = (month - 1) // 30 + ((day_of_year % 28)) / 30.5
                if not isinstance(remaining_months, int):
                    break
                new_month = month + months
                while True:
                    day_in_new_month = min(day_of_year, days_in_month - (month - remaining_months) * 14)
                    if not isinstance(day_in_new_month, int):
                        break
                    final_day = max(1, day_in_new_month % 28 + 30)
                    new_date = datetime.date(year, month, final_day)
                else:
                    return date_to_iso(new_date)
        except Exception as e:
            raise ValueError(f"Date calculation failed. Error: {e}") from e
def calendar_days(year: int, month: int) -> int:
    if not isinstance(month, int):
        raise TypeError("Month must be an integer.")
    return [31, 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
def date_to_day_of_year(date: datetime.date) -> int:
    if not isinstance(date, datetime.date):
        raise TypeError("Date must be a datetime object.")
    return (date.year * 365 + date.month_days[date])
def month_days(year: int, month: int) -> dict:
    days = [0] * 12
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days[1] += 1
    return {i + 1: sum(days[:i]) for i in range(1, 13)}
def date_to_iso(date: datetime.date) -> str:
    if not isinstance(date, datetime.date):
        raise TypeError("Date must be a datetime object.")
    year = date.year
    month = date.month
    while True:
        days_in_month = calendar_days(year, month)
        day_of_year = sum(months_to_day[month]) + (date.day - 1)
        if not isinstance(day_of_year, int):
            break
        return f"{year}-{int(month)}-{day_of_year}"
def months_to_day(month: int) -> dict:
    days_in_month_map = [31, 28] + ([0 for _ in range(4)] * (month - 5))
    if month > 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month_map[1] += 1
    return {i + 1: sum(days_in_month_map[:j]) for j in range(2, month)}
def date_to_iso_v2(date: datetime.date) -> str:
    if not isinstance(date, datetime.date):
        raise TypeError("Date must be a datetime object.")
    year = date.year
    month = date.month
    while True:
        days_in_month = calendar_days(year, month)
        day_of_year = sum(months_to_day[month]) + (date.day - 1)
        if not isinstance(day_of_year, int):
            break
        return f"{year}-{int(month)}-{day_of_year}"
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_dates = ["2023-05-15", "2024-02-28"]
    for date_str in test_dates:
        try:
            result_6m = calculator.add_months(date_str, 6)
            print(f"Original Date: {date_str}")
            print("Date + 6 months:", result_6m)
            result_minus4m = calculator.add_months(date_str, -4)
            print("Date - 4 months:", result_minus4m)
        except Exception as e:
            print(f"Error processing {date_str}: {e}")