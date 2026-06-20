from datetime import datetime

def format_datetime(dt):
    return dt.strftime('%d/%m/%Y %I:%M %p')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 26, 15, 45)
    formatted_date = format_datetime(sample_dt)
    print(formatted_date)