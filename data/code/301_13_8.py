import datetime

def is_valid_iso_date(date_str: str) -> bool:
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def iso_to_readable_date(iso_date: str) -> str:
    dt_object = datetime.datetime.strptime(iso_date, '%Y-%m-%d')
    return dt_object.strftime('%d %B %Y')

if __name__ == '__main__':
    sample_iso_date = '2021-07-04'
    if is_valid_iso_date(sample_iso_date):
        formatted_date = iso_to_readable_date(sample_iso_date)
        print(formatted_date)