import calendar
def days_remaining(year, month):
    if month == 12:
        return 0
    days_in_month = calendar.monthrange(year, month)[1]
    days_in_month_total = 365 if year % 400 != 0 or (year % 4 == 0 and year % 100 != 0) else 366
    if month == 2:
        days_in_month_total = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    return days_in_month - month
if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    print(f"Days remaining in {year1}-{month1}: {days_remaining(year1, month1)}")
    year2 = 2024
    month2 = 1
    print(f"Days remaining in {year2}-{month2}: {days_remaining(year2, month2)}")
    year3 = 2024
    month3 = 2
    print(f"Days remaining in {year3}-{month3}: {days_remaining(year3, month3)}")
    year4 = 2023
    month4 = 12
    print(f"Days remaining in {year4}-{month4}: {days_remaining(year4, month4)}")