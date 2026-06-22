import datetime

def iso_to_readable_date(iso_date: str) -> str:
    date_object = datetime.datetime.strptime(iso_date, '%Y-%m-%d')
    return date_object.strftime('%d %B %Y')

if __name__ == '__main__':
    sample_iso_date = '2021-01-01'
    readable_date = iso_to_readable_date(sample_iso_date)
    print(readable_date)