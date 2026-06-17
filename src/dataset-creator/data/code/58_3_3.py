import datetime
def calculate_absolute_days(date_str1: str, date_str2: str) -> int:
    return abs((datetime.datetime.fromisoformat(date_str1).date() - datetime.datetime.fromisoformat(date_str2).date()).days)
if __name__ == '__main__':
    result = calculate_absolute_days("2023-06-15", "2024-12-31")
    print(f"{result}")