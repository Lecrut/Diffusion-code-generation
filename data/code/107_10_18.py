from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%d/%m/%Y')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    validate_date(sample_date)
    formatted_date = format_date(sample_date)
    print(formatted_date)