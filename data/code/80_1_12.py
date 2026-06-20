from datetime import datetime

def compare_dates(date1: str, date2: str) -> datetime:
    try:
        return min(datetime.strptime(date1, '%Y-%m-%d'), datetime.strptime(date2, '%Y-%m-%d'))
    except ValueError as e:
        print(f"Invalid date format: {e}")
        raise

if __name__ == '__main__':
    earlier_date = compare_dates('2023-04-01', '2023-05-01')
    print(earlier_date)