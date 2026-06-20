import calendar

def month_difference(month1, month2):
    return abs(calendar.monthrange(2023, month1)[1] - calendar.monthrange(2023, month2)[1])

if __name__ == '__main__':
    print(month_difference(1, 12))