def calculate_day_of_year(date_tuple):
    year, month, day = date_tuple
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    return sum(days_in_month[:month-1]) + day

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