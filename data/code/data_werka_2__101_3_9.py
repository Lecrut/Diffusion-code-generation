from datetime import datetime

def get_weekday(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%A")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

if __name__ == '__main__':
    result = get_weekday("2023-12-25")
    print(result)