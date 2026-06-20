import datetime

def calculate_day_of_year(date_tuple):
    year, month, day = date_tuple
    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError("Invalid date")
    if month == 2:
        is_leap = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
        max_day = 29 if is_leap else 28
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:
        max_day = 31
    if day > max_day:
        raise ValueError("Invalid date")
    return (datetime.date(year, month, day) - datetime.date(year, 1, 1)).days + 1

if __name__ == '__main__':
    date1 = (2024, 3, 15)
    date2 = (2000, 1, 1)
    date3 = (2023, 12, 31)
    date4 = (2024, 2, 29)
    date5 = (2023, 1, 1)
    print(f"Day of year for {date1}: {calculate_day_of_year(date1)}")
    print(f"Day of year for {date2}: {calculate_day_of_year(date2)}")
    print(f"Day of year for {date3}: {calculate_day_of_year(date3)}")
    print(f"Day of year for {date4}: {calculate_day_of_year(date4)}")
    print(f"Day of year for {date5}: {calculate_day_of_year(date5)}")