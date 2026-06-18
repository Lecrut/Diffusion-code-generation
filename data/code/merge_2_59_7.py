import datetime
def get_weekday_name(date_str: str) -> str:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-06-18", "2025-01-01"]
    for date_str in sample_dates:
        print(f"{date_str} -> {get_weekday_name(date_str)}")