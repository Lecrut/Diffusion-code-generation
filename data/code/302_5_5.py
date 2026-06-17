def calculate_day(month, year):
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28
if __name__ == '__main__':
    year1 = 2024
    month1 = 2
    print(f"{month1} in {year1}: {calculate_day(month1, year1)}")
    year2 = 2000
    month2 = 2
    print(f"{month2} in {year2}: {calculate_day(month2, year2)}")
    year3 = 2023
    month3 = 4
    print(f"{month3} in {year3}: {calculate_day(month3, year3)}")
    year4 = 1900
    month4 = 2
    print(f"{month4} in {year4}: {calculate_day(month4, year4)}")
    year5 = 2024
    month5 = 1
    print(f"{month5} in {year5}: {calculate_day(month5, year5)}")