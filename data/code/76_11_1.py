import datetime
def calculate_days(start_date_str, end_date_str):
    start_date = datetime.datetime.fromisoformat(start_date_str)
    end_date = datetime.datetime.fromisoformat(end_date_str)
    return (end_date - start_date).days
if __name__ == '__main__':
    start = "2023-01-01T00:00:00"
    end = "2023-01-10T00:00:00"
    days = calculate_days(start, end)
    print(days)