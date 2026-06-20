def calculate_day_of_year(year, month, day):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days_in_month[2] = 29
    return sum(days_in_month[:month]) + day
if __name__ == '__main__':
    print(calculate_day_of_year(2023, 10, 5))