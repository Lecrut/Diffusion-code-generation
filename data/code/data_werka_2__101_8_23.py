import calendar

def get_weekday_for_date(date_info):
    yr, mo, dy = date_info
    day_code = calendar.weekday(yr, mo, dy)
    day_title = calendar.day_name[day_code]
    return day_title

if __name__ == '__main__':
    my_date = (1989, 9, 13)
    day_name = get_weekday_for_date(my_date)
    print(day_name)