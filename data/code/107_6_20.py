from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def format_date(date_str):
    if not validate_date(date_str):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%A, %B %d, %Y')
    return formatted_date

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(format_date(sample_date))