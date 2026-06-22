import datetime

def is_weekend(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_obj.weekday() >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please provide a date in the format 'YYYY-MM-DD'.")

if __name__ == '__main__':
    date_to_check = '2023-10-07'
    print(f"Is {date_to_check} a weekend? {is_weekend(date_to_check)}")