import calendar

def check_weekday(year, month, day):
    try:
        day_index = calendar.weekday(year, month, day)
        return day_index < 5
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")

if __name__ == '__main__':
    valid_date = check_weekday(2023, 10, 23)
    print(valid_date)
    invalid_date = check_weekday(2023, 2, 29)
    print(invalid_date)