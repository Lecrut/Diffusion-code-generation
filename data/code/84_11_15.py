import calendar

def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def calculate_day_of_year(date_tuple):
    year, month, day = date_tuple
    if not (1 <= month <= 12 and 1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError("Invalid date")
    return datetime.datetime(year, month, day).timetuple().tm_yday

if __name__ == '__main__':
    print(f"Day of year for (2024, 3, 15): {calculate_day_of_year((2024, 3, 15))}")
    print(f"Day of year for (2000, 1, 1): {calculate_day_of_year((2000, 1, 1))}")
    print(f"Day of year for (2023, 12, 31): {calculate_day_of_year((2023, 12, 31))}")
    print(f"Day of year for (2024, 2, 29): {calculate_day_of_year((2024, 2, 29))}")
    print(f"Day of year for (2023, 1, 1): {calculate_day_of_year((2023, 1, 1))}")