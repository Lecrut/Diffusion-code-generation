import calendar
def days_remaining(year, month):
    days_in_month = calendar.monthrange(year, month)[1]
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    days_in_next_month = calendar.monthrange(next_year, next_month)[1]
    return days_in_next_month - 1
if __name__ == '__main__':
    test_cases = [
        (2023, 1),                                                          
        (2024, 2),                                                          
        (2024, 12),                                                                      
        (2023, 12),                                                                      
        (2024, 1),                                                          
    ]
    for year, month in test_cases:
        result = days_remaining(year, month)
        print(f"Days remaining after {month}/{year}: {result}")