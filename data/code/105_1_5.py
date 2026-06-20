def first_sunday_after_jan_1():
    start_date = 2024
    while True:
        if start_date % 4 == 0 and start_date % 100 != 0 or start_date % 400 == 0:
            days_in_year = 366
        else:
            days_in_year = 365
        for day in range(1, days_in_year + 1):
            if (day - 1) % 7 == 6:
                return f'{start_date}-{day:02d}'
        start_date += 1
if __name__ == '__main__':
    print(first_sunday_after_jan_1())