def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_day_of_year(year, month, day):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        months[1] = 29
    day_of_year = sum(months[:month - 1]) + day
    return day_of_year

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = calculate_day_of_year(year, month, day)
    print(result)