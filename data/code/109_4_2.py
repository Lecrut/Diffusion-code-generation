from datetime import date
def days_remaining_in_month(current_date):
    year = current_date.year
    month = current_date.month
    if month == 12:
        days_in_month = 31
    else:
        import calendar
        days_in_month = calendar.monthrange(year, month)[1]
    days_passed = current_date.day
    days_remaining = days_in_month - days_passed
    return days_remaining
if __name__ == '__main__':
    test_date_1 = date(2023, 10, 15)
    result_1 = days_remaining_in_month(test_date_1)
    print(f"For {test_date_1}, days remaining: {result_1}")
    test_date_2 = date(2024, 1, 1)
    result_2 = days_remaining_in_month(test_date_2)
    print(f"For {test_date_2}, days remaining: {result_2}")
    test_date_3 = date(2023, 12, 31)
    result_3 = days_remaining_in_month(test_date_3)
    print(f"For {test_date_3}, days remaining: {result_3}")
    test_date_4 = date(2024, 2, 10)
    result_4 = days_remaining_in_month(test_date_4)
    print(f"For {test_date_4}, days remaining: {result_4}")