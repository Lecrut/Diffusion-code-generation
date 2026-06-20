from datetime import date

def days_remaining_in_month(current_date):
    year = current_date.year
    month = current_date.month
    if month == 12:
        last_day_of_month = date(year, 12, 31)
    else:
        next_month = month + 1
        next_year = year
        if next_month > 12:
            next_month = 1
            next_year += 1
        last_day_of_month = date(next_year, next_month, 1) - timedelta(days=1)
    
    days_passed = current_date.day
    days_remaining = (last_day_of_month - current_date).days + 1
    return days_remaining

if __name__ == '__main__':
    test_date_1 = date(2023, 10, 15)
    result_1 = days_remaining_in_month(test_date_1)
    print(f"For {test_date_1}, days remaining: {result_1}")
    
    test_date_2 = date(2024, 1, 1)
    result_2 = days_remaining_in_month(test_date_2)
    print(f"For {test_date_2}, days remaining: {result_2}")