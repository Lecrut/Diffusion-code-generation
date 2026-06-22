def days_in_month(year, month):
    if month == 2:
        is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return 29 if is_leap_year else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

if __name__ == '__main__':
    year1 = 2020
    month1 = 2
    result1 = days_in_month(year1, month1)
    print(f"Days in {year1}-{month1}: {result1}")

    year2 = 2019
    month2 = 2
    result2 = days_in_month(year2, month2)
    print(f"Days in {year2}-{month2}: {result2}")

    year3 = 2021
    month3 = 4
    result3 = days_in_month(year3, month3)
    print(f"Days in {year3}-{month3}: {result3}")