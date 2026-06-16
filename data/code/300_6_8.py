import calendar
def days_remaining(year, month):
    days_in_month = calendar.monthrange(year, month)[1]
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return (365 if next_month != 1 else 366) - (days_in_month - 1)
if __name__ == '__main__':
    test_cases = [
        (2023, 1),                                                                                                                           
        (2023, 12),                                                                                                                          
        (2024, 2),                                 
        (2024, 3),                      
        (2025, 1),                      
        (2023, 2),                      
    ]
    results = []
    for year, month in test_cases:
        days_in_month = calendar.monthrange(year, month)[1]
        if month == 12:
            remaining = 0
        else:
            remaining = days_in_month
        results.append((year, month, remaining))
    print("Test Cases:")
    for year, month, result in results:
        print(f"Year: {year}, Month: {month}, Days Remaining (Length): {result}")