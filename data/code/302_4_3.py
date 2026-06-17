import datetime
def get_day_of_month(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("All inputs must be integers")
    if year < 1 or month < 1 or month > 12 or day < 1:
        raise ValueError("Invalid date provided")
    return day
if __name__ == '__main__':
    date1 = (2023, 10, 15)
    print(f"Date {date1[0]}-{date1[1]}-{date1[2]}: Day of month is {get_day_of_month(*date1)}")
    date2 = (2024, 1, 1)
    print(f"Date {date2[0]}-{date2[1]}-{date2[2]}: Day of month is {get_day_of_month(*date2)}")
    date3 = (2025, 12, 31)
    print(f"Date {date3[0]}-{date3[1]}-{date3[2]}: Day of month is {get_day_of_month(*date3)}")
    try:
        get_day_of_month(2023, 13, 1)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        get_day_of_month(2023, 10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        get_day_of_month("2023", 10, 15)
    except TypeError as e:
        print(f"Error caught: {e}")