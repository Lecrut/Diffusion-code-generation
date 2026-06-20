from datetime import datetime

def format_to_rfc2822(date_obj):
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be a datetime object.")
    
    return date_obj.strftime("%a, %d %b %Y %H:%M:%S %z")

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30)
    print(format_to_rfc2822(sample_date))