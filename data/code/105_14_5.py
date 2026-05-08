import calendar
def date_one_year_later(year, month, day):
    if month == 12:
        new_month = 1
        new_year = year + 1
    else:
        new_month = month + 1
        new_year = year
    try:
        new_day = day
        if new_month == 2:
            is_leap = calendar.isleap(new_year)
            if is_leap:
                new_day = min(new_day, 29)
            else:
                new_day = min(new_day, 28)
        elif new_month in [4, 6, 9, 11]:
            is_leap = calendar.isleap(new_year)
            max_day = 30 if new_month == 4 or new_month == 6 or new_month == 9 or new_month == 11 else 31
            if is_leap:
                if new_month == 2:
                    max_day = 29
                elif new_month == 4 or new_month == 6 or new_month == 9 or new_month == 11:
                    max_day = 30
            new_day = min(new_day, max_day)
        elif new_month == 2:
            if calendar.isleap(new_year):
                new_day = min(new_day, 29)
            else:
                new_day = min(new_day, 28)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if calendar.isleap(new_year):
            days_in_month[2] = 29
        new_day = min(day, days_in_month[new_month])
        return new_year, new_month, new_day
    except Exception:
        return None, None, None
if __name__ == '__main__':
    date1 = (2023, 10, 26)
    print(f"One year after {date1}: {date_one_year_later(*date1)}")
    date2 = (2024, 2, 29)
    print(f"One year after {date2}: {date_one_year_later(*date2)}")
    date3 = (2023, 12, 31)
    print(f"One year after {date3}: {date_one_year_later(*date3)}")
    date4 = (2023, 1, 1)
    print(f"One year after {date4}: {date_one_year_later(*date4)}")
    date5 = (2024, 11, 30)
    print(f"One year after {date5}: {date_one_year_later(*date5)}")