from datetime import date

def is_before(date1: date, date2: date) -> bool:
    return date1 < date2

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 26)
    sample_date2 = date(2023, 10, 20)
    print(is_before(sample_date1, sample_date2))