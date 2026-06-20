from datetime import datetime

def compare_dates(date1, date2):
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Both inputs must be instances of datetime.")
    
    if date1 < date2:
        return "First is earlier"
    elif date1 > date2:
        return "Second is earlier"
    else:
        return "They are equal"

if __name__ == '__main__':
    date1 = datetime(2023, 1, 15)
    date2 = datetime(2023, 2, 1)
    result1 = compare_dates(date1, date2)
    print(result1)

    date1 = datetime(2023, 2, 1)
    date2 = datetime(2023, 1, 15)
    result2 = compare_dates(date1, date2)
    print(result2)

    date1 = datetime(2023, 10, 20)
    date2 = datetime(2023, 10, 20)
    result3 = compare_dates(date1, date2)
    print(result3)