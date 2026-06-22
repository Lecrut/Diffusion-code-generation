from datetime import datetime

HOLIDAYS = {
    "2023-10-12": True,
}

def is_weekend_or_holiday(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    weekday = date_obj.weekday()
    return weekday >= 5 or HOLIDAYS.get(date_str, False)

if __name__ == '__main__':
    sample_date = "2023-10-12"
    print(is_weekend_or_holiday(sample_date))