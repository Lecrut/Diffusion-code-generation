from datetime import datetime

def format_rfc2822(date):
    if not isinstance(date, datetime):
        raise ValueError("Input must be a datetime object.")
    
    return date.strftime('%a, %d %b %Y %H:%M:%S %z')

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30)
    print(format_rfc2822(sample_date))