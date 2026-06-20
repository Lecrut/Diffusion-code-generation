from datetime import date

def calculate_month_difference(month1, month2):
    year = 2023
    date1 = date(year, month1, 1)
    date2 = date(year, month2, 1)
    return abs((date2 - date1).days) // 30
if __name__ == '__main__':
    print(calculate_month_difference(1, 6))