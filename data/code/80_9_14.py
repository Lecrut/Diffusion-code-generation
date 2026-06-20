from datetime import datetime

def compare_dates(date1: str, date2: str) -> str:
    try:
        date_format = "%Y-%m-%d"
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)
        if d1 < d2:
            return date1
        elif d1 > d2:
            return date2
        else:
            return "Both dates are the same."
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    print(compare_dates("2023-01-01", "2023-01-02"))
    print(compare_dates("2023-01-02", "2023-01-01"))
    print(compare_dates("2023-01-01", "2023-01-01"))
    print(compare_dates("2023-01-01", "2023-02-01"))
    print(compare_dates("2023-01-01", "2022-12-31"))
    print(compare_dates("2023-01-01", "invalid-date"))