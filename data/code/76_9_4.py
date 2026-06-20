from datetime import datetime

def days_between(start_date: str, end_date: str) -> int:
    start = datetime.fromisoformat(start_date)
    end = datetime.fromisoformat(end_date)
    delta = end - start
    return abs(delta.days)

if __name__ == '__main__':
    print(days_between('2023-01-01', '2023-01-31'))