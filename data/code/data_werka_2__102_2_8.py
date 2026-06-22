from datetime import date

def is_weekday(d: date) -> bool:
    return d.weekday() < 5

if __name__ == '__main__':
    print(is_weekday(date(2023, 10, 23)))
    print(is_weekday(date(2023, 10, 21)))