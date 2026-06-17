import calendar
def days_remaining(year, month):
    if month == 12:
        return 0
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month
if __name__ == '__main__':
    year1 = 2024
    month1 = 3
    print(f"Days remaining in {year1}-{month1}: {days_remaining(year1, month1)}")
    year2 = 2023
    month2 = 2
    print(f"Days remaining in {year2}-{month2}: {days_remaining(year2, month2)}")
    year3 = 2024
    month3 = 12
    print(f"Days remaining in {year3}-{month3}: {days_remaining(year3, month3)}")