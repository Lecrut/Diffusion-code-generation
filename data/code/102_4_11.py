from datetime import datetime

def is_weekday(timestamp: str) -> bool:
    try:
        date_obj = datetime.strptime(timestamp, '%Y-%m-%d')
        return 0 <= date_obj.weekday() <= 4
    except ValueError:
        raise ValueError("Invalid Date Format")

if __name__ == '__main__':
    sample_dates = [
        "2023-10-23",
        "2023-10-29",
        "2023-10-28",
        "2023-10-27",
        "2023-10-28",
        "2023-10-30"
    ]
    
    for date in sample_dates:
        try:
            print(f"{date}: {is_weekday(date)}")
        except ValueError as e:
            print(e)