def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, is_leap=False):
    months = [31, 28 if not is_leap else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month - 1]

def calculate_day_of_year(year, month, day):
    if day < 1 or day > days_in_month(month, is_leap_year(year)):
        raise ValueError("Invalid date")
    
    previous_months_days = sum(days_in_month(m, is_leap_year(year)) for m in range(1, month))
    return previous_months_days + day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    sample_day = 15
    result = calculate_day_of_year(sample_year, sample_month, sample_day)
    print(result)