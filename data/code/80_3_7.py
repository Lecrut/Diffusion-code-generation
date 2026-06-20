from datetime import date

def is_strictly_before(date1: date, date2: date) -> bool:
    return date1 < date2

if __name__ == '__main__':
    print(is_strictly_before(date(2023, 1, 1), date(2023, 1, 2)))