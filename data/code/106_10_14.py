from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    if date1 == date2:
        return 0
    start_date = date1 if date1 < date2 else date2
    end_date = date2 if date1 < date2 else date1
    years = end_date.year - start_date.year
    if end_date.month < start_date.month:
        years -= 1
    elif end_date.month == start_date.month:
        if end_date.day < start_date.day:
            years -= 1
    return years

if __name__ == '__main__':
    d1 = datetime(2000, 2, 29)
    d2 = datetime(2024, 2, 28)
    result = calculate_year_difference(d1, d2)
    print(result)