from datetime import datetime

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    years = end_date.year - start_date.year
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
    return years

if __name__ == '__main__':
    start = datetime(2000, 1, 1)
    end = datetime(2023, 12, 31)
    result = calculate_year_difference(start, end)
    print(result)