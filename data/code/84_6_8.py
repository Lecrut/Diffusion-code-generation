import calendar

def find_day_of_year(year, month, day):
    return calendar.timegm((year, month, day, 0, 0, 0, 0, 0, 0)) // (60 * 60 * 24) + 1

if __name__ == '__main__':
    print(find_day_of_year(2023, 10, 5))