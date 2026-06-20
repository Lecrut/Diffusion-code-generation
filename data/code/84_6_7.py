import calendar

def day_of_year(year, month, day):
    return calendar.timegm((year, month, day, 0, 0, 0, 0, 0, 0)) // (24 * 60 * 60) + 1

if __name__ == '__main__':
    print(day_of_year(2023, 10, 5))