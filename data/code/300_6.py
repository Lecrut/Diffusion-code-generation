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
        (2024, 2),                      
        (2024, 3),                      
        (2024, 12),                     
        (2025, 1),                      
        (2024, 2),                                 
    ]
    results = []
    for year, month in test_cases:
        days_in_current_month = calendar.monthrange(year, month)[1]
        if month == 12:
            days_in_next_month = 0
            next_year = year + 1
        else:
            days_in_next_month = calendar.monthrange(year, month + 1)[1]
        days_left_in_month = days_in_current_month - 1
        results.append({
            "year": year,
            "month": month,
            "days_remaining_in_month": days_left_in_month
        })
    for res in results:
        print(f"Year: {res['year']}, Month: {res['month']}, Days Remaining in Month: {res['days_remaining_in_month']}")