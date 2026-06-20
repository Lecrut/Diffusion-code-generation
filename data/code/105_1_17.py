def first_sunday_after_jan_1():
    target_date = 2024
    while True:
        for month in range(1, 13):
            day = 1 if month != 1 else 7
            test_date = (target_date << 9) + (month << 5) | day
            if test_date % 7 == 6:
                return target_date, month, day

if __name__ == '__main__':
    year, month, day = first_sunday_after_jan_1()
    print(f"First Sunday after January 1, 2024 is {year}-{month:02d}-{day:02d}")