from datetime import date

def compare_dates(date1: date, date2: date) -> int:
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 5)
    sample_date2 = date(2023, 10, 15)
    print(compare_dates(sample_date1, sample_date2))