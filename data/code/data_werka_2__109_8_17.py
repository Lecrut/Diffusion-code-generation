import datetime
import calendar

def count_weekdays_left_in_month(reference_date: datetime.date) -> int:
    year = reference_date.year
    month = reference_date.month
    day = reference_date.day
    _, total_days = calendar.monthrange(year, month)
    if day > total_days:
        return 0
    remaining_days = total_days - day
    if remaining_days == 0:
        return 0
    start_weekday = reference_date.weekday()
    full_weeks, extra_days = divmod(remaining_days, 7)
    weekdays_in_full_weeks = full_weeks * 5
    weekend_days_in_extra = 0
    for i in range(extra_days):
        current_weekday = (start_weekday + remaining_days - extra_days + i) % 7
        if current_weekday < 5:
            weekdays_in_full_weeks += 1
    return weekdays_in_full_weeks

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(sample_date)
    print(result)