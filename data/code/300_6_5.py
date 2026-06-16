import calendar
def days_remaining(year, month):
    total_days_in_year = 366 if calendar.isleap(year) else 365
    days_passed = calendar.monthrange(year, month)[1]
    days_in_month = calendar.monthrange(year, month)[0]
    days_remaining_in_month = days_in_month - days_passed
    return days_remaining_in_month
if __name__ == '__main__':
    test_cases = [
        (2023, 1, 31),                                                
        (2023, 2, 28),                                                 
        (2024, 2, 29),                                             
        (2024, 3, 1),                                                
        (2025, 12, 31),                                                
        (2020, 2, 28)                                              
    ]
    for year, month, day in test_cases:
        result = days_remaining(year, month)
        print(f"Days remaining in {year}-{month}: {result}")