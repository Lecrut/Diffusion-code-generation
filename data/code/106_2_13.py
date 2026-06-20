from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    year_diff = abs((date2.year - date1.year))
    if (date2.month, date2.day) < (date1.month, date1.day):
        year_diff -= 1
    return year_diff

if __name__ == '__main__':
    date1 = datetime(2000, 5, 15)
    date2 = datetime(2023, 8, 20)
    difference = calculate_year_difference(date1, date2)
    print(difference)