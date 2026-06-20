from datetime import datetime

def calculate_year_difference(date1, date2):
    return abs(date2.year - date1.year + (date2.month > date1.month or (date2.month == date1.month and date2.day >= date1.day)))
if __name__ == '__main__':
    date1 = datetime(2020, 2, 29)
    date2 = datetime(2023, 2, 28)
    print(calculate_year_difference(date1, date2))