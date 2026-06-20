from datetime import datetime

def year_difference(date1: datetime, date2: datetime) -> int:
    return abs(date1.year - date2.year)

if __name__ == '__main__':
    date1 = datetime(2020, 1, 1)
    date2 = datetime(2015, 1, 1)
    print(year_difference(date1, date2))