from datetime import date

def is_weekday(d: date) -> bool:
    return d.weekday() < 5

if __name__ == '__main__':
    sample_date = date(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)