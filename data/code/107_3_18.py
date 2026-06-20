import datetime

def format_rfc2822(date):
    return date.strftime('%a, %d %b %Y %H:%M:%S %z')

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30)
    print(format_rfc2822(sample_date))