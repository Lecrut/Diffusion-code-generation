from datetime import datetime

def calculate_month_difference(month1, month2):
    year = 2023
    date1 = datetime(year, list(month_to_num.keys()).index(month1) + 1, 1)
    date2 = datetime(year, list(month_to_num.keys()).index(month2) + 1, 1)
    return abs((date2 - date1).days // 30)
month_to_num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))