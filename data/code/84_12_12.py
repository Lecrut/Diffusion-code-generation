from datetime import date

def get_day_of_year(year, month, day):
    return date(year, month, day).timetuple().tm_yday

if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    day1 = 27
    result1 = get_day_of_year(year1, month1, day1)
    print(f"Day of the year for {year1}-{month1:02d}-{day1:02d} is: {result1}")