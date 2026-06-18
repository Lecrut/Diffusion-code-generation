import datetime
def calculate_days_between(date1: str, date2: str) -> int:
    return abs((datetime.datetime.fromisoformat(date1).date() - datetime.datetime.fromisoformat(date2).date()).days)
if __name__ == '__main__':
    result = calculate_days_between("2023-06-15", "2024-07-20")
    print(f"{result}")