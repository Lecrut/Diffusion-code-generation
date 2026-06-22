import calendar

def check_weekday(year, month, day):
    day_index = calendar.weekday(year, month, day)
    is_workday = day_index < 5
    return is_workday

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 5
    sample_day = 20
    weekday_status = check_weekday(sample_year, sample_month, sample_day)
    print(weekday_status)