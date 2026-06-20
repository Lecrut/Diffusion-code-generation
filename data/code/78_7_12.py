import calendar

def calculate_month_difference(month1, month2):
    year = 2023
    days_in_month1 = calendar.monthrange(year, month1)[1]
    days_in_month2 = calendar.monthrange(year, month2)[1]
    difference = abs(days_in_month1 - days_in_month2)
    return difference

if __name__ == '__main__':
    result = calculate_month_difference(3, 7)
    print(result)