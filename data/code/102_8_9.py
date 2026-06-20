from datetime import date

def is_weekday(iso_date_str):
    try:
        date_obj = date.fromisoformat(iso_date_str)
        return date_obj.weekday() < 5
    except ValueError:
        raise ValueError('Invalid ISO format date string')
if __name__ == '__main__':
    print(is_weekday('2023-10-25'))
    print(is_weekday('2023-10-28'))
    print(is_weekday('2023-10-29'))