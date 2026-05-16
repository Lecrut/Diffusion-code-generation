import datetime
def calculate_day_of_year(date_obj):
    year = date_obj.year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 366
            else:
                return 365
        else:
            return 366
    else:
        return 365
if __name__ == '__main__':
    date1 = datetime.date(2024, 3, 15)
    date2 = datetime.date(2000, 1, 1)
    date3 = datetime.date(2023, 12, 31)
    date4 = datetime.date(2024, 2, 29)
    date5 = datetime.date(1900, 3, 1)
    print(f"Day of year for {date1}: {calculate_day_of_year(date1)}")
    print(f"Day of year for {date2}: {calculate_day_of_year(date2)}")
    print(f"Day of year for {date3}: {calculate_day_of_year(date3)}")
    print(f"Day of year for {date4}: {calculate_day_of_year(date4)}")
    print(f"Day of year for {date5}: {calculate_day_of_year(date5)}")