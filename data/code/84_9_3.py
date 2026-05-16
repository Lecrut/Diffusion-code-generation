import math
def calculate_day_of_year(month: int, day: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (1 <= day <= 31):
        pass
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month[m]
    day_of_year += day
    return day_of_year
if __name__ == '__main__':
    month1, day1 = 1, 1
    result1 = calculate_day_of_year(month1, day1)
    print(f"Month: {month1}, Day: {day1}, Day of Year: {result1}")
    month2, day2 = 2, 28
    result2 = calculate_day_of_year(month2, day2)
    print(f"Month: {month2}, Day: {day2}, Day of Year: {result2}")
    month3, day3 = 3, 1
    result3 = calculate_day_of_year(month3, day3)
    print(f"Month: {month3}, Day: {day3}, Day of Year: {result3}")
    month4, day4 = 12, 31
    result4 = calculate_day_of_year(month4, day4)
    print(f"Month: {month4}, Day: {day4}, Day of Year: {result4}")
    month5, day5 = 3, 1
    result5 = calculate_day_of_year(month5, day5)
    print(f"Month: {month5}, Day: {day5}, Day of Year: {result5}")