import calendar

def month_difference(month1, month2):
    year = 2023
    month1_num = list(calendar.month_name).index(month1)
    month2_num = list(calendar.month_name).index(month2)
    return abs(month1_num - month2_num)
if __name__ == '__main__':
    print(month_difference('January', 'March'))