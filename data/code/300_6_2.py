import calendar
def days_remaining(year, month):
    days_in_month = calendar.monthrange(year, month)[1]
    if month == 12:
        return 0
    return days_in_month - month
if __name__ == '__main__':
    test_cases = [
        (2023, 1),                            
        (2023, 7),                            
        (2024, 2),                                       
        (2024, 3),                            
        (2025, 12),                          
        (2000, 1),                                       
    ]
    for year, month in test_cases:
        result = days_remaining(year, month)
        print(f"Days remaining in {year}-{month}: {result}")