import datetime

def get_day_of_month(date_str):
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return dt.day

if __name__ == '__main__':
    dates = ["2023-10-01", "2024-02-29", "2025-12-25"]
    for d in dates:
        print(get_day_of_month(d))