import calendar

def get_weekday_name(date_tuple):
    year, month, day = date_tuple
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    sample_date = (2023, 10, 5)
    result = get_weekday_name(sample_date)
    print(result)