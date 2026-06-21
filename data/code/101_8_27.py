import calendar

def get_weekday_name_from_tuple(date_data):
    year, month, day = date_data
    day_number = calendar.weekday(year, month, day)
    return calendar.day_name[day_number]

if __name__ == '__main__':
    test_date = (2025, 12, 25)
    weekday_name = get_weekday_name_from_tuple(test_date)
    print(weekday_name)