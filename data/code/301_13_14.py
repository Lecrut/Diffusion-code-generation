from datetime import datetime

def iso_to_readable(date_str: str) -> str:
    dt_object = datetime.strptime(date_str, '%Y-%m-%d')
    return dt_object.strftime('%d %B %Y')

if __name__ == '__main__':
    sample_date = '2021-01-01'
    readable_date = iso_to_readable(sample_date)
    print(readable_date)