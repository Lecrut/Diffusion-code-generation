import datetime

def calculate_date_difference(start_date: str, end_date: str) -> int:
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    return abs((end - start).days)

if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2024-01-01"
    difference = calculate_date_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {difference} days")