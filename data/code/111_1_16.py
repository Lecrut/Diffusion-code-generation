from datetime import date, timedelta

def add_days_to_july_4() -> str:
    base = date(2024, 7, 4)
    delta = timedelta(days=30)
    future = base + delta
    return future.strftime("%Y-%m-%d")

if __name__ == '__main__':
    result = add_days_to_july_4()
    print(result)