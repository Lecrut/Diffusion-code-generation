import datetime
def calculate_day_of_year(date_obj):
    year = date_obj.year
    if year % 400 == 0:
        is_leap = (year % 4 == 0)
    else:
        is_leap = (year % 4 == 0)
    day_of_year = (date_obj.timetuple().tm_yday)
    return day_of_year
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 26)
    date2 = datetime.date(2000, 3, 1)
    date3 = datetime.date(2024, 2, 29)
    date4 = datetime.date(2023, 1, 1)
    print(f"Day of year for {date1}: {calculate_day_of_year(date1)}")
    print(f"Day of year for {date2}: {calculate_day_of_year(date2)}")
    print(f"Day of year for {date3}: {calculate_day_of_year(date3)}")
    print(f"Day of year for {date4}: {calculate_day_of_year(date4)}")