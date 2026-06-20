from datetime import date

def day_of_year(year, month, day):
    return date(year, month, day).timetuple().tm_yday

if __name__ == '__main__':
    print(day_of_year(2023, 10, 5))