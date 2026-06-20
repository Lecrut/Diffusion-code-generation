import datetime

def get_day_of_week(year, month=1, day=1):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise ValueError("Year, month, and day must be integers.")
    
    date_obj = datetime.datetime(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    year = 2024
    print(get_day_of_week(year))