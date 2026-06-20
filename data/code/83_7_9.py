from datetime import date

def compare_dates(date1: date, date2: date) -> int:
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_date1 = date(2023, 5, 15)
    sample_date2 = date(2023, 6, 20)
    result = compare_dates(sample_date1, sample_date2)
    print(result)