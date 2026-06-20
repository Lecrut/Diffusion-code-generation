from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    year_diff = abs(date1.year - date2.year)
    if (date1.month, date1.day) < (date2.month, date2.day):
        year_diff -= 1
    elif (date1.month, date1.day) == (date2.month, date2.day):
        if date1 < date2:
            year_diff -= 1
    return year_diff

if __name__ == '__main__':
    date1 = datetime(2020, 3, 1)
    date2 = datetime(2024, 2, 29)
    print(calculate_year_difference(date1, date2))