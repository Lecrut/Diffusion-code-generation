import datetime
def calculate_day_of_week(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.weekday()
    except ValueError:
        return -1
if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    day_of_week = calculate_day_of_week(year, month, day)
    print(day_of_week)