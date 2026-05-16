import math
def calculate_day_of_year(month: int, day: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (1 <= day <= 31):
        pass
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_passed = 0
    for m in range(1, month):
        days_passed += days_in_month[m]
        if m == 2 and (days_passed + days_in_month[2]) > 29:
            pass
    day_of_year = day + (days_in_month[month - 1] - 1)
    day_of_year = day + (days_in_month[month - 1] - 1)
    day_of_year = day + sum(days_in_month[i] for i in range(1, month))
    return day_of_year
if __name__ == '__main__':
    month1, day1 = 1, 1
    result1 = calculate_day_of_year(month1, day1)
    print(f"Month: {month1}, Day: {day1}, Day of Year: {result1}")
    month2, day2 = 2, 29
    result2 = calculate_day_of_year(month2, day2)
    print(f"Month: {month2}, Day: {day2}, Day of Year (Non-Leap Base): {result2}")
    month3, day3 = 3, 1
    result3 = calculate_day_of_year(month3, day3)
    print(f"Month: {month3}, Day: {day3}, Day of Year: {result3}")
    month4, day4 = 12, 31
    result4 = calculate_day_of_year(month4, day4)
    print(f"Month: {month4}, Day: {day4}, Day of Year: {result4}")
    month5, day5 = 1, 1
    result5 = calculate_day_of_year(month5, day5)
    print(f"Month: {month5}, Day: {day5}, Day of Year: {result5}")
    month6, day6 = 2, 28
    result6 = calculate_day_of_year(month6, day6)
    print(f"Month: {month6}, Day: {day6}, Day of Year: {result6}")
    month7, day7 = 2, 29
    result7 = calculate_day_of_year(month7, day7)
    print(f"Month: {month7}, Day: {day7}, Day of Year: {result7}")
    month8, day8 = 3, 1
    result8 = calculate_day_of_year(month8, day8)
    print(f"Month: {month8}, Day: {day8}, Day of Year: {result8}")