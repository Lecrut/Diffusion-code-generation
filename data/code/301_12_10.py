from datetime import datetime

def format_datetime(date_obj):
    return date_obj.strftime("%A, %B %d, %Y")

if __name__ == '__main__':
    sample_date = datetime(2023, 12, 31)
    formatted_date = format_datetime(sample_date)
    print(formatted_date)