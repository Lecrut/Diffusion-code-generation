import calendar

def month_difference(month1, month2):
    year = 2023
    month1_days = calendar.monthrange(year, month1)[1]
    month2_days = calendar.monthrange(year, month2)[1]
    return abs(month1_days - month2_days)

if __name__ == '__main__':
    print(month_difference(1, 12))