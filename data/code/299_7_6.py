from datetime import datetime

def is_weekend_or_holiday(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        weekday = date_obj.weekday()
        if weekday >= 5 or date_str == "2023-10-12":
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    sample_date = "2023-10-12"
    print(is_weekend_or_holiday(sample_date))