from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def format_date(date_str):
    if not validate_date(date_str):
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%d/%m/%Y')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    formatted_date = format_date(sample_date)
    print(formatted_date)