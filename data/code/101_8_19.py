import calendar

def get_weekday_name(year, month, day):
    weekday_num = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_num]

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 27
    print(get_weekday_name(sample_year, sample_month, sample_day))