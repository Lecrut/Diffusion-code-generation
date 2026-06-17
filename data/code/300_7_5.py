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
    yield year, results
if __name__ == '__main__':
    sample_year = 2023
    gen = remaining_days_per_month(sample_year)
    output = list(gen)
    print(f"Year: {output[0][0]}")
    print("Remaining days per month (simplified calculation):")
    for year, results in output:
        print(results)