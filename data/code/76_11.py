from datetime import datetime
def calculate_days(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    return (end_date - start_date).days
if __name__ == '__main__':
    start = "2023-01-01"
    end = "2023-01-31"
    days = calculate_days(start, end)
    print(days)