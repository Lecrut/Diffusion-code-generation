from datetime import datetime

def get_day_of_week(date_string: str) -> int:
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.weekday()

if __name__ == '__main__':
    print(get_day_of_week("2023-10-23"))
    print(get_day_of_week("2024-01-01"))
    print(get_day_of_week("2000-02-29"))