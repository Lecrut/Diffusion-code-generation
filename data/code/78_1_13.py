from datetime import date

def calculate_month_difference(month1, month2):
    year = 2023
    date1 = date(year, list(date.__dict__.keys()).index(month1) + 1, 1)
    date2 = date(year, list(date.__dict__.keys()).index(month2) + 1, 1)
    return abs((date1.year - date2.year) * 12 + (date1.month - date2.month))
if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))