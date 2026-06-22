from datetime import date

def is_weekend(date_str):
    try:
        parsed_date = date.fromisoformat(date_str)
        return parsed_date.weekday() >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    dates = ['2023-10-06', '2023-10-07', '2023-10-08']
    for d in dates:
        print(f"Is {d} a weekend? {is_weekend(d)}")