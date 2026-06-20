import calendar

def get_day_of_week(year, month, day):
    weekday_number = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_number]

if __name__ == '__main__':
    sample_date_year = 2023
    sample_date_month = 12
    sample_date_day = 25
    result = get_day_of_week(sample_date_year, sample_date_month, sample_date_day)
    print(f"The day of the week for {sample_date_month}/{sample_date_year} is {result}.")