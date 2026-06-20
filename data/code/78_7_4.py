import datetime

def calculate_month_difference(month1, month2):
    year = 2023
    date1 = datetime.date(year, month1, 1)
    date2 = datetime.date(year, month2, 1)
    difference = abs((date2 - date1).days) // 30
    return difference
if __name__ == '__main__':
    result = calculate_month_difference(5, 8)
    print(result)