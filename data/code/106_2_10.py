from datetime import datetime

def year_difference(date1, date2):
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date1 = datetime(2010, 5, 15)
    date2 = datetime(2023, 8, 20)
    print(year_difference(date1, date2))