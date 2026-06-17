def remaining_days_per_month(year):
    results = []
    for month in range(1, 13):
        if month == 1:
            days = 31
        elif month == 2:
            days = 28 if year % 4 != 0 or year % 100 != 0 or year % 400 != 0 else 29
        elif month == 3:
            days = 31
        elif month == 4:
            days = 30
        elif month == 5:
            days = 31
        elif month == 6:
            days = 30
        elif month == 7:
            days = 31
        elif month == 8:
            days = 31
        elif month == 9:
            days = 30
        elif month == 10:
            days = 31
        elif month == 11:
            days = 30
        elif month == 12:
            days = 31
        if month == 1:
            remaining = days - 1                                                                                                                                                                                                                                                                                
            results.append(days)
    yielded_results = []
    for month in range(1, 13):
        if month == 1:
            days = 31
        elif month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            days = 29 if is_leap else 28
        elif month in [3, 5, 7, 8, 10, 12]:
            days = 31
        elif month in [4, 6, 9, 11]:
            days = 30
        else:
            continue
        yield days
if __name__ == '__main__':
    sample_year = 2024
    print(f"Remaining days for the year {sample_year}:")
    for days in remaining_days_per_month(sample_year):
        print(days)