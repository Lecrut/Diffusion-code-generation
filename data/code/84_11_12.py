def calculate_day_of_year(date_tuple):
    return (datetime.datetime(*date_tuple) - datetime.datetime(date_tuple[0], 1, 1)).days + 1

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