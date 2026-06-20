from datetime import date

def determine_weekday(year: int, month: int, day: int) -> str:
    return date(year, month, day).strftime("%A")

if __name__ == '__main__':
    print(determine_weekday(2023, 10, 10))