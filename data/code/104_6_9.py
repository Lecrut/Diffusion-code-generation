from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        if date1 < date2:
            return "date1 is earlier"
        elif date1 > date2:
            return "date1 is later"
        else:
            return "dates are the same"
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    print(compare_dates("2023-01-15", "2023-03-01"))
    print(compare_dates("2023-01-15", "2023-01-01"))
    print(compare_dates("2024-05-20", "2024-03-10"))
    print(compare_dates("2023-01-15", "invalid-date"))