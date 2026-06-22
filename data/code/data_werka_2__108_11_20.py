from datetime import date

def get_day_of_month(d: date) -> int:
    if not isinstance(d, date):
        raise ValueError("Expected a date object")
    return d.day

if __name__ == '__main__':
    target_date = date(2023, 3, 15)
    print(get_day_of_month(target_date))