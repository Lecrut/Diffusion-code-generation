import calendar
def days_remaining(year, month):
    if month == 12:
        return 0
    days_in_month = calendar.monthrange(year, month)[1]
    if month < 12:
        days_in_year = (366 if calendar.isleap(year) else 365)
    else:
        days_in_year = 366 if calendar.isleap(year) else 365
    days_passed = 0
    if month > 1:
        for m in range(1, month):
            days_passed += calendar.monthrange(year, m)[1]
    days_remaining_in_month = days_in_month - (days_passed + 1)
    return days_remaining_in_month
if __name__ == '__main__':
    test_cases = [
        (2023, 1),                                      
        (2023, 12),                                    
        (2024, 2),                                                 
        (2024, 3),                                      
        (2025, 1),                                      
        (2025, 12),                                    
        (2023, 2),                                      
    ]
    for year, month in test_cases:
        result = days_remaining(year, month)
        print(f"Days remaining in {year}-{month}: {result}")