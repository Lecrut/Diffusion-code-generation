from datetime import datetime

def day_of_year(year=2023, month=4, day=15):
    date = datetime(year, month, day)
    return date.timetuple().tm_yday

if __name__ == '__main__':
    print(day_of_year())