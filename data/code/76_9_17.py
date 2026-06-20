import datetime

def calculate_days_between(start_date_str: str, end_date_str: str) -> int:
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
    return abs((end_date - start_date).days)

if __name__ == '__main__':
    date_a = '2023-01-01'
    date_b = '2024-01-01'
    difference = calculate_days_between(date_a, date_b)
    print(f"Days between {date_a} and {date_b}: {difference}")