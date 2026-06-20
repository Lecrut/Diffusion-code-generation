from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Inputs must be instances of datetime.")
    
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date1 = datetime(1980, 6, 7)
    date2 = datetime(2023, 4, 15)
    difference = calculate_year_difference(date1, date2)
    print(difference)