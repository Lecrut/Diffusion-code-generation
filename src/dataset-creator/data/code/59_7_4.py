import datetime
def get_weekday_name(date_str: str) -> str:
    date_obj = datetime.datetime.fromisoformat(date_str)
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-06-18", "2025-12-31"]
    for date in sample_dates:
        print(f"{date}: {get_weekday_name(date)}")