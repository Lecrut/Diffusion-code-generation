import calendar

def get_day_of_year(year, month, day):
    return calendar.timegm((year, month, day, 0, 0, 0, 0, 0, 0)) % 365 + 1

if __name__ == '__main__':
    print(get_day_of_year(2023, 4, 1))