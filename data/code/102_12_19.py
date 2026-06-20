import datetime

def is_weekday(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.weekday() < 5
    except ValueError:
        return False

if __name__ == '__main__':
    dates = {
        "2023-10-25": True,
        "2023-10-26": True,
        "2023-10-27": True,
        "2023-10-28": True,
        "2023-10-29": True,
        "2023/10/25": False
    }
    
    for date, expected in dates.items():
        print(f"Is {date} a weekday? {is_weekday(date)} (Expected: {expected})")