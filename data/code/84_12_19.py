from datetime import date

def calculate_day_of_year(year, month, day):
    target_date = date(year, month, day)
    start_of_year = date(year, 1, 1)
    return (target_date - start_of_year).days + 1

if __name__ == '__main__':
    year2 = 2023
    month2 = 10
    day2 = 27
    result2 = calculate_day_of_year(year2, month2, day2)
    print(f"Day of the year for {year2}-{month2:02d}-{day2:02d} is: {result2}")