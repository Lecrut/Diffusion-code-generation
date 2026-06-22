import datetime

def is_weekend(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_obj.weekday() >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please provide the date in 'YYYY-MM-DD' format.")

if __name__ == '__main__':
    print(f"Is 2023-10-07 a weekend? {is_weekend('2023-10-07')}")