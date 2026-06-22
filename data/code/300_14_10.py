def days_in_month(year, month):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    print(f"Year: {year1}, Month: {month1}, Days in month: {days_in_month(year1, month1)}")
    
    year2 = 2024
    month2 = 2
    print(f"Year: {year2}, Month: {month2}, Days in month: {days_in_month(year2, month2)}")