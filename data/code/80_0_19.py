from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        return date1 < date2
    except ValueError:
        return None

if __name__ == '__main__':
    print(compare_dates("2023-01-01", "2023-01-02"))