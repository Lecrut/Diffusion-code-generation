import calendar

def validate_date(year, month, day):
    if not (1 <= month <= 12) or not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError("Invalid date")

def get_day_of_week(year, month, day):
    validate_date(year, month, day)
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 12
    sample_day = 25
    print(f"The day of the week for {sample_month}/{sample_year} is {get_day_of_week(sample_year, sample_month, sample_day)}.")