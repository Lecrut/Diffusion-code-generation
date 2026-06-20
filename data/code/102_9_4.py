from datetime import date

def is_weekday(year, month, day):
    return date(year, month, day).weekday() < 5
if __name__ == '__main__':
    print(is_weekday(2023, 10, 5))
    print(is_weekday(2023, 10, 6))