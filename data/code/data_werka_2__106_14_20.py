from datetime import datetime

def get_year_difference(date1: datetime, date2: datetime) -> int:
    return abs(date1.year - date2.year)

if __name__ == '__main__':
    d1 = datetime(2023, 10, 15)
    d2 = datetime(2018, 5, 20)
    result = get_year_difference(d1, d2)
    print(result)