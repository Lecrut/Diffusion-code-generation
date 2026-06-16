def feb_day(year):
    return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
if __name__ == '__main__':
    print(feb_day(2024))
    print(feb_day(2023))
    print(feb_day(2100))
    print(feb_day(2000))