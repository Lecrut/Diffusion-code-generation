from datetime import datetime

def get_day_of_month(date_strings):
    results = []
    for date_str in date_strings:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        results.append(dt.day)
    return results

if __name__ == '__main__':
    dates = ["2023-10-15", "2024-02-29", "2025-12-25"]
    days = get_day_of_month(dates)
    print(days)