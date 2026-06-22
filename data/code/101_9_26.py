from datetime import datetime

def get_day_of_week(date_str):
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    return parsed_date.strftime("%A").upper()

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date string provided: {date_str}")

if __name__ == '__main__':
    target_date = "2023-11-11"
    validate_date_format(target_date)
    day = get_day_of_week(target_date)
    print(day)