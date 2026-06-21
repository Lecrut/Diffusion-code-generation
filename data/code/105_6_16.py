from datetime import date, timedelta

def next_seven_day_date():
    start = date(2024, 1, 1)
    offset = 7
    return start + timedelta(days=offset)

if __name__ == '__main__':
    result = next_seven_day_date()
    print(result)