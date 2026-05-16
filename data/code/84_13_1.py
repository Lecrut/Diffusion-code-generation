import datetime
calculate_day_of_year = lambda y, m, d: datetime.date(y, m, d).timetuple().tm_yday
if __name__ == '__main__':
    year, month, day = 2023, 10, 26
    day_of_year = calculate_day_of_year(year, month, day)
    print(day_of_year)