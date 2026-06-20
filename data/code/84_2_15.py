def day_of_year(year, month, day):
    return (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400 + [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month] + (month > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

if __name__ == '__main__':
    print(day_of_year(2023, 10, 27))