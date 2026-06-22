def days_in_month(year, month):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return months[month] + 1
    return months[month]

if __name__ == '__main__':
    print(days_in_month(2020, 2))
    print(days_in_month(2019, 2))
    print(days_in_month(2021, 4))