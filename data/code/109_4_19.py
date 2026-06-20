from datetime import date

def days_in_month(year: int, month: int) -> int:
    if month == 12:
        return 31
    else:
        next_month = (month % 12) + 1
        return (date(year + next_month // 12, next_month % 12 + 1, 1) - date(year, month, 1)).days

def days_remaining_in_current_month(target_date: date) -> int:
    today = date.today()
    if target_date.year < today.year or (target_date.year == today.year and target_date.month < today.month):
        raise ValueError("Target date is in the past")
    
    current_year = target_date.year
    current_month = target_date.month
    
    days_in_current_month = days_in_month(current_year, current_month)
    days_passed = target_date.day
    
    return days_in_current_month - days_passed

if __name__ == '__main__':
    test_date_1 = date(2023, 10, 15)
    result_1 = days_remaining_in_current_month(test_date_1)
    print(f"For {test_date_1}, days remaining: {result_1}")
    
    test_date_2 = date(2024, 1, 1)
    result_2 = days_remaining_in_current_month(test_date_2)
    print(f"For {test_date_2}, days remaining: {result_2}")