from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    sample_date1 = datetime(2020, 1, 1)
    sample_date2 = datetime(2023, 4, 15)
    print(calculate_year_difference(sample_date1, sample_date2))