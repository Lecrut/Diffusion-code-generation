import datetime
def get_day_of_month(date_string: str) -> int:
    try:
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return date_object.day
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    date1 = "2023-10-27"
    date2 = "1999-01-01"
    date3 = "2024-02-29"
    date4 = "2023-12-31"
    print(f"Day of month for {date1}: {get_day_of_month(date1)}")
    print(f"Day of month for {date2}: {get_day_of_month(date2)}")
    print(f"Day of month for {date3}: {get_day_of_month(date3)}")
    print(f"Day of month for {date4}: {get_day_of_month(date4)}")