from datetime import date

def get_day_of_month(year: int, month: int, day: int) -> int:
    return date(year, month, day).day

if __name__ == '__main__':
    print(get_day_of_month(2024, 10, 10))