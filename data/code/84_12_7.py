import datetime

def day_of_year(year, month, day):
    date = datetime.date(year, month, day)
    return date.timetuple().tm_yday

if __name__ == '__main__':
    print(day_of_year(2023, 10, 5))