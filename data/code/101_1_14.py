import calendar

def get_weekday_name(year, month, day):
    date_obj = calendar.datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    year1, month1, day1 = 2023, 10, 26
    year2, month2, day2 = 2024, 1, 1
    year3, month3, day3 = 2025, 12, 31
    
    print(get_weekday_name(year1, month1, day1))
    print(get_weekday_name(year2, month2, day2))
    print(get_weekday_name(year3, month3, day3))