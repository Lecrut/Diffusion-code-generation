from datetime import datetime

def iso_date_to_readable(iso_date: str) -> str:
    dt_object = datetime.strptime(iso_date, '%Y-%m-%d')
    return dt_object.strftime('%d %B %Y')

if __name__ == '__main__':
    sample_iso_date = '2021-01-01'
    readable_date = iso_date_to_readable(sample_iso_date)
    print(readable_date)