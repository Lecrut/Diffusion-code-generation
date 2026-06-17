def remaining_days_per_month(year):
    results = []
    for month in range(1, 13):
        if month == 1:
            days_in_month = 31
        elif month == 2:
            days_in_month = 28 if year % 4 != 0 or year % 100 != 0 or year % 400 != 0 else 29
        elif month == 3:
            days_in_month = 31
        elif month == 4:
            days_in_month = 30
        elif month == 5:
            days_in_month = 31
        elif month == 6:
            days_in_month = 30
        elif month == 7:
            days_in_month = 31
        elif month == 8:
            days_in_month = 31
        elif month == 9:
            days_in_month = 30
        elif month == 10:
            days_in_month = 31
        elif month == 11:
            days_in_month = 30
        elif month == 12:
            days_in_month = 31
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if month == 2:
            days_in_month = 29 if is_leap else 28
        results.append(days_in_month)
    return iter(results)
if __name__ == '__main__':
    sample_year = 2024
    day_generator = remaining_days_per_month(sample_year)
    print(f"Remaining days for each month in {sample_year}:")
    for i, days in enumerate(day_generator):
        print(f"Month {i + 1}: {days} days")