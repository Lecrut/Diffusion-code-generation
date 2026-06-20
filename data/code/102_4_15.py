from datetime import datetime

def is_weekday(date_string: str) -> bool:
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return 0 <= date_obj.weekday() <= 4
    except ValueError:
        return False

if __name__ == '__main__':
    dates = ["2023-10-23", "2023-10-29", "2023-10-28", "2023-10-27", "2023-10-28", "2023-10-30"]
    for date in dates:
        print(f"{date}: {is_weekday(date)}")