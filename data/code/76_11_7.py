from datetime import date

DAYS_PER_MONTH = 30

def days_between(start_date_str: str, end_date_str: str) -> int:
    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)
    return (end_date - start_date).days

if __name__ == '__main__':
    start = "2023-01-01"
    end = "2023-01-31"
    days = days_between(start, end)
    print(days)