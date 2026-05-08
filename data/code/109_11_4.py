import datetime
def calculate_days_remaining(target_month, target_day, current_year):
    target_date = datetime.date(current_year, target_month, 1)
    if target_day > 31:
        return -1
    try:
        end_of_month = datetime.date(current_year, target_month, 1) + datetime.timedelta(days=31)
    except ValueError:
        if target_month == 2:
            end_of_month = datetime.date(current_year, target_month, 29) if (datetime.date(current_year, target_month, 29) in [datetime.date(current_year, target_month, 29), datetime.date(current_year + 1, 1, 1)]) else datetime.date(current_year, target_month, 28)
        else:
            end_of_month = datetime.date(current_year, target_month, 31)
    if target_month == 12:
        days_in_month = 31
    elif target_month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        days_in_month = 31
    days_remaining = days_in_month - target_day
    if days_remaining < 0:
        return -1
    return days_remaining
if __name__ == '__main__':
    current_year = 2023
    target_month1 = 10
    target_day1 = 15
    result1 = calculate_days_remaining(target_month1, target_day1, current_year)
    print(f"Days remaining until end of {target_month1}/{target_day1} in {current_year}: {result1}")
    target_month2 = 12
    target_day2 = 31
    result2 = calculate_days_remaining(target_month2, target_day2, current_year)
    print(f"Days remaining until end of {target_month2}/{target_day2} in {current_year}: {result2}")
    target_month3 = 2
    target_day3 = 28
    result3 = calculate_days_remaining(target_month3, target_day3, current_year)
    print(f"Days remaining until end of {target_month3}/{target_day3} in {current_year}: {result3}")
    target_month4 = 3
    target_day4 = 30
    result4 = calculate_days_remaining(target_month4, target_day4, current_year)
    print(f"Days remaining until end of {target_month4}/{target_day4} in {current_year}: {result4}")