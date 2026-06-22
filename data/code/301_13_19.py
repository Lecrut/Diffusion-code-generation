import datetime

def iso_to_readable_date(iso_date: str) -> str:
    try:
        dt_object = datetime.datetime.strptime(iso_date, '%Y-%m-%d')
        return dt_object.strftime('%d %B %Y')
    except ValueError:
        raise ValueError("Invalid ISO date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    sample_date = '2021-01-01'
    readable_date = iso_to_readable_date(sample_date)
    print(readable_date)