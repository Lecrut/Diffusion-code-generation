from datetime import datetime

def calculate_year_difference(date1, date2):
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    date1 = datetime(2010, 5, 15)
    date2 = datetime(2023, 8, 20)
    print(calculate_year_difference(date1, date2))