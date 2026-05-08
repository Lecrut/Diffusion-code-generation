from datetime import date
def days_remaining(current_date):
    today = date.today()
    current_month = today.month
    current_year = today.year
    if current_month == today.month:
        return 0
    else:
        next_month = today.month + 1
        next_year = today.year
        if next_month > 12:
            next_month = 1
            next_year += 1
        import calendar
        days_in_current_month = calendar.monthrange(current_year, current_month)[1]
        days_passed = today.day
        days_remaining = days_in_current_month - days_passed
        if days_remaining <= 0:
            return 0
        else:
            return days_remaining
if __name__ == '__main__':
    sample_date_1 = date(2023, 10, 15)
    print(f"Days remaining for {sample_date_1}: {days_remaining(sample_date_1)}")
    sample_date_2 = date(2023, 10, 31)
    print(f"Days remaining for {sample_date_2}: {days_remaining(sample_date_2)}")
    sample_date_3 = date(2023, 10, 1)
    print(f"Days remaining for {sample_date_3}: {days_remaining(sample_date_3)}")
    sample_date_4 = date(2023, 11, 10)
    print(f"Days remaining for {sample_date_4}: {days_remaining(sample_date_4)}")
    sample_date_5 = date(2023, 12, 1)
    print(f"Days remaining for {sample_date_5}: {days_remaining(sample_date_5)}")