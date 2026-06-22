import datetime

def check_weekday(date_str: str) -> bool:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_obj.weekday() < 5

if __name__ == '__main__':
    dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    results = [check_weekday(d) for d in dates]
    print(results)