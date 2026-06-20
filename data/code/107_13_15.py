from datetime import datetime

def validate_date_format(date_str):
    if not isinstance(date_str, str) or len(date_str) != 10 or date_str[4] != '/' or date_str[7] != '/':
        raise ValueError("Invalid date format. Expected 'YYYY/MM/DD'")
    
    try:
        datetime.strptime(date_str, '%Y/%m/%d')
    except ValueError:
        raise ValueError("Date string is not in a valid 'YYYY/MM/DD' format")

def format_date(date_str):
    validate_date_format(date_str)
    return datetime.strptime(date_str, '%Y/%m/%d').strftime('%B %d, %Y')

if __name__ == '__main__':
    sample_date = '2023/10/05'
    formatted_date = format_date(sample_date)
    print(formatted_date)