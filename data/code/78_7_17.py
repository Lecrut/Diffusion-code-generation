import calendar

def calculate_month_difference(month1, month2):
    year = 2023
    month1_days = calendar.monthrange(year, month1)[1]
    month2_days = calendar.monthrange(year, month2)[1]
    return abs(month2 - month1)

if __name__ == '__main__':
    result = calculate_month_difference(1, 6)
    print(result)