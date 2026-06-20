from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date1 = datetime(2015, 7, 4)
    date2 = datetime(2030, 11, 25)
    difference = calculate_year_difference(date1, date2)
    print(difference)