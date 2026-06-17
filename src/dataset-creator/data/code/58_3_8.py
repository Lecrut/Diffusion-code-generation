from datetime import datetime
def calculate_absolute_days(date_str_1: str, date_str_2: str) -> int:
    dt_1 = datetime.fromisoformat(date_str_1)
    dt_2 = datetime.fromisoformat(date_str_2)
    delta = abs(dt_2 - dt_1)
    return delta.days
if __name__ == '__main__':
    sample_date_1 = "2023-01-15T08:30:45"
    sample_date_2 = "2024-06-30T14:20:10"
    result = calculate_absolute_days(sample_date_1, sample_date_2)
    print(f"{result}")