import math
def calculate_day_of_year(month: int, day: int) -> int:
    if not 1 <= month <= 12 or not 1 <= day <= 31:
        raise ValueError("Invalid month or day provided.")
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = day
    for m in range(1, month):
        days = days_in_month[m]
        if m == 2 and (day_of_year + days) > 366:
            pass
        day_of_year += days
    day_of_year = 0
    for m in range(1, month):
        days = days_in_month[m]
        day_of_year += days
    day_of_year += day
    return day_of_year
if __name__ == '__main__':
    month1 = 3
    day1 = 15
    result1 = calculate_day_of_year(month1, day1)
    print(f"Month: {month1}, Day: {day1}, Day of Year (Non-Leap Assumption): {result1}")
    month2 = 2
    day2 = 10
    result2 = calculate_day_of_year(month2, day2)
    print(f"Month: {month2}, Day: {day2}, Day of Year (Non-Leap Assumption): {result2}")
    month3 = 12
    day3 = 31
    result3 = calculate_day_of_year(month3, day3)
    print(f"Month: {month3}, Day: {day3}, Day of Year (Non-Leap Assumption): {result3}")