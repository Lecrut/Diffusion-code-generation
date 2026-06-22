from datetime import date, timedelta

def get_next_7day_multiple():
    start_date = date(2024, 1, 1)
    delta = timedelta(days=7)
    next_date = start_date + delta
    return next_date

if __name__ == '__main__':
    result = get_next_7day_multiple()
    print(result)