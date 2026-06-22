from datetime import datetime

def format_date(date_obj):
    return date_obj.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    result = format_date(sample_date)
    print(result)