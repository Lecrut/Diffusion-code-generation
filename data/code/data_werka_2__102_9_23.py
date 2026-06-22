import datetime

def is_weekday(date_str: str) -> bool:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_obj.weekday() < 5

if __name__ == '__main__':
    dates = ["2023-10-07", "2023-10-08", "2023-10-09"]
    results = [is_weekday(d) for d in dates]
    print(results)