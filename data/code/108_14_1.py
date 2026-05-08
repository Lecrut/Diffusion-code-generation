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
    print(get_day_of_month(date1))
    print(get_day_of_month(date2))
    print(get_day_of_month(date3))