from datetime import datetime

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    return end_date.year - start_date.year

if __name__ == '__main__':
    start = datetime(2010, 5, 15)
    end = datetime(2023, 8, 20)
    result = calculate_year_difference(start, end)
    print(result)