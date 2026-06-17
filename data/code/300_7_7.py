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
        else:
            remaining = days
        results.append(remaining)
    return iter(results)
def day_generator(year):
    days_in_month = [0] * 12
    for month in range(1, 13):
        if month == 1:
            days_in_month[0] = 31
        elif month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            days_in_month[1] = 29 if is_leap else 28
        elif month == 3:
            days_in_month[2] = 31
        elif month == 4:
            days_in_month[3] = 30
        elif month == 5:
            days_in_month[4] = 31
        elif month == 6:
            days_in_month[5] = 30
        elif month == 7:
            days_in_month[6] = 31
        elif month == 8:
            days_in_month[7] = 31
        elif month == 9:
            days_in_month[8] = 30
        elif month == 10:
            days_in_month[9] = 31
        elif month == 11:
            days_in_month[10] = 30
        elif month == 12:
            days_in_month[11] = 31
    for i in range(12):
        yield days_in_month[i]
if __name__ == '__main__':
    sample_year = 2024
    generator = day_generator(sample_year)
    print(f"Remaining days for each month in {sample_year}:")
    for days in generator:
        print(days)