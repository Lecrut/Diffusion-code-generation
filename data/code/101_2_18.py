def calculate_day_of_week(year, month, day):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        days_in_month[2] = 29
    if day < 1 or day > days_in_month[month]:
        raise ValueError("Day is out of range for the given month and year")
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]

if __name__ == '__main__':
    result = calculate_day_of_week(2024, 2, 29)
    print(result)