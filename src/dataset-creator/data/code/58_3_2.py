import datetime
def calculate_days_between(date1: str, date2: str) -> int:
    dt1 = datetime.datetime.fromisoformat(date1).date()
    dt2 = datetime.datetime.fromisoformat(date2).date()
    return abs((dt2 - dt1).days)
if __name__ == '__main__':
    result = calculate_days_between("2023-06-15", "2024-07-20")
    print(f"{result}")