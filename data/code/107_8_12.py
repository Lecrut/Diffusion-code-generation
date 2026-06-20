from datetime import datetime

def format_datetime_to_localized(dt):
    return dt.strftime('%d/%m/%Y %I:%M %p')

if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 26, 14, 35)
    formatted_date = format_datetime_to_localized(sample_datetime)
    print(formatted_date)