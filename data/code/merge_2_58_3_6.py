import datetime
def calculate_days_between(date1_str: str, date2_str: str) -> int:
    return abs((datetime.datetime.fromisoformat(date1_str).date() - datetime.datetime.fromisoformat(date2_str).date()).days)
if __name__ == '__main__':
    result = calculate_days_between("2023-06-15", "2024-07-20")
    print(f"{result}")