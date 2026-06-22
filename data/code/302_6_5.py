def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if is_leap_year(year) else 28

if __name__ == '__main__':
    year1 = 2020
    month1 = 2
    result1 = days_in_month(year1, month1)
    print(f"Year: {year1}, Month: {month1}, Days in month: {result1}")
    
    year2 = 2021
    month2 = 4
    result2 = days_in_month(year2, month2)
    print(f"Year: {year2}, Month: {month2}, Days in month: {result2}")
    
    year3 = 2023
    month3 = 1
    result3 = days_in_month(year3, month3)
    print(f"Year: {year3}, Month: {month3}, Days in month: {result3}")