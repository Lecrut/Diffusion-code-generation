from datetime import date

def day_of_year(year=2023, month=4, day=1):
    return date(year, month, day).timetuple().tm_yday

if __name__ == '__main__':
    print(day_of_year())