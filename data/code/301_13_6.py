from datetime import datetime

def iso_to_readable_date(iso_date: str) -> str:
    try:
        date_obj = datetime.strptime(iso_date, '%Y-%m-%d')
        return date_obj.strftime('%d %B %Y')
    except ValueError:
        raise ValueError("Invalid ISO date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    sample_iso_date = '2021-01-01'
    try:
        readable_date = iso_to_readable_date(sample_iso_date)
        print(readable_date)
    except ValueError as e:
        print(e)