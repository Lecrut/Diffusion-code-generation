import calendar

def get_day_of_week(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 12
    sample_day = 25
    print(f"The day of the week for {sample_month}/{sample_day}/{sample_year} is {get_day_of_week(sample_year, sample_month, sample_day)}.")