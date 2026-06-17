import datetime
def get_weekday_name(date_str: str) -> str:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_dates = ["2024-01-01", "2024-03-15", "2024-06-20"]
    for d in sample_dates:
        print(f"{d} -> {get_weekday_name(d)}")