days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEAR_THRESHOLD_4 = 4
LEAP_YEAR_THRESHOLD_100 = 100
LEAP_YEAR_THRESHOLD_400 = 400

def is_leap_year(year):
    return (year % LEAP_YEAR_THRESHOLD_4 == 0 and year % LEAP_YEAR_THRESHOLD_100 != 0) or (year % LEAP_YEAR_THRESHOLD_400 == 0)

def calculate_day_of_year(year, month, day):
    if month > 2 and is_leap_year(year):
        days_in_month[1] = 29
    return sum(days_in_month[:month - 1]) + day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    sample_day = 15
    result = calculate_day_of_year(sample_year, sample_month, sample_day)
    print(result)