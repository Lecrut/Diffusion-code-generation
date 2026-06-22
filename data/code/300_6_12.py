from datetime import date

def days_remaining(year, month):
    if not (1 <= year <= 9999) or not (1 <= month <= 12):
        raise ValueError("Invalid year or month")
    
    today = date.today()
    last_day_of_month = date(year, month, 1) + timedelta(days=31)
    last_day_of_month -= timedelta(days=last_day_of_month.day)
    
    return (last_day_of_month - today).days

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