from datetime import datetime

def format_datetime(dt):
    return dt.strftime('%d/%m/%Y %I:%M %p')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30)
    print(format_datetime(sample_dt))