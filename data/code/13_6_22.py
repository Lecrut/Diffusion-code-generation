from datetime import date

def days_between_dates(date1: str, date2: str) -> int:
    start_date = date.fromisoformat(date1)
    end_date = date.fromisoformat(date2)
    delta = end_date - start_date
    return abs(delta.days)
if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2024-02-29'
    print(days_between_dates(date1, date2))