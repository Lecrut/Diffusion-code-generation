import datetime

def calculate_day_of_year(year=2023, month=4, day=1):
    date = datetime.date(year, month, day)
    return date.timetuple().tm_yday

if __name__ == '__main__':
    print(calculate_day_of_year())