from datetime import datetime

def get_days_of_month(date_strings):
    days = []
    for s in date_strings:
        dt = datetime.strptime(s, "%Y-%m-%d")
        days.append(dt.day)
    return days

if __name__ == '__main__':
    dates = ["2023-01-15", "2024-02-29", "2025-12-31"]
    result = get_days_of_month(dates)
    print(result)