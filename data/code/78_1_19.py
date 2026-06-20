from datetime import datetime

def calculate_month_difference(month1, month2):
    year = 2023
    date1 = datetime(year, list(enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']))[month1].index + 1, 1)
    date2 = datetime(year, list(enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']))[month2].index + 1, 1)
    return abs((date2 - date1).days // 30)
if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))