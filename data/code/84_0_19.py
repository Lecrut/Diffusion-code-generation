def calculate_day_of_year(year, month, day):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:month - 1]) + day
if __name__ == '__main__':
    print(calculate_day_of_year(2024, 2, 29))