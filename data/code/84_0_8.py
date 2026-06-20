def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_day_of_year(year, month, day):
    if not (1 <= month <= 12) or not (1 <= day <= 31):
        raise ValueError("Invalid date")
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    
    return sum(days_in_month[:month - 1]) + day

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = calculate_day_of_year(year, month, day)
    print(result)