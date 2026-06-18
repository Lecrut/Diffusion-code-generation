import datetime
def calculate_days_between(date_str1: str, date_str2: str) -> int:
    dt1 = datetime.datetime.fromisoformat(date_str1).date()
    dt2 = datetime.datetime.fromisoformat(date_str2).date()
    return abs((dt2 - dt1).days)
if __name__ == '__main__':
    date_a = "2023-06-15"
    date_b = "2024-01-10"
    result = calculate_days_between(date_a, date_b)
    print(f"{result=}")