from datetime import date

def is_weekday(iso_date):
    date_obj = date.fromisoformat(iso_date)
    return date_obj.weekday() < 5

if __name__ == '__main__':
    print(f"Is {date(2023, 10, 25).isoformat()} a weekday? {is_weekday(date(2023, 10, 25).isoformat())}")
    print(f"Is {date(2023, 10, 28).isoformat()} a weekday? {is_weekday(date(2023, 10, 28).isoformat())}")