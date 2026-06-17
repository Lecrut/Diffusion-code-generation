import datetime
def calculate_days_between(date_str_1: str, date_str_2: str) -> int:
    return abs((datetime.datetime.fromisoformat(date_str_1).date() - datetime.datetime.fromisoformat(date_str_2).date()).days)
if __name__ == '__main__':
    result = calculate_days_between("2023-06-15", "2024-08-20")
    print(result)