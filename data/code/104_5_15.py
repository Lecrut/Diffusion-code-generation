from datetime import datetime

def compare_dates(date1_str, date2_str):
    DATE_FORMAT = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, DATE_FORMAT)
    date2 = datetime.strptime(date2_str, DATE_FORMAT)
    
    if date1 < date2:
        return "First is earlier"
    elif date2 < date1:
        return "Second is earlier"
    else:
        return "They are equal"

if __name__ == '__main__':
    print(compare_dates("2023-01-15", "2023-02-01"))
    print(compare_dates("2023-02-01", "2023-01-15"))
    print(compare_dates("2023-10-20", "2023-10-20"))