from datetime import date

def is_weekend(date_str):
    try:
        date_obj = date.fromisoformat(date_str)
        return date_obj.weekday() >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please provide a date in 'YYYY-MM-DD' format.")

if __name__ == '__main__':
    dates_to_check = ['2023-10-06', '2023-10-07', '2023-10-08']
    for date_str in dates_to_check:
        print(f"Is {date_str} a weekend? {is_weekend(date_str)}")