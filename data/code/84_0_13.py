def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(month, year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return months[month - 1]

def calculate_day_of_year(year, month, day):
    total_days = sum(days_in_month(m, year) for m in range(1, month))
    return total_days + day

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = calculate_day_of_year(year, month, day)
    print(result)