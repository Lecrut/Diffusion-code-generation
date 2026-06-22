from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def format_dates(date_list):
    for date_str in date_list:
        if validate_date(date_str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%B %d, %Y')
            print(formatted_date)
        else:
            print(f"Invalid date format: {date_str}")

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-12-25', '2024-07-04', 'invalid-date']
    format_dates(sample_dates)