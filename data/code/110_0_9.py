from datetime import datetime

def validate_date_string(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

def sort_dates_chronologically(date_list):
    if not isinstance(date_list, list):
        raise TypeError("Input must be a list")
    for d in date_list:
        validate_date_string(d)
    return sorted(date_list, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))

if __name__ == '__main__':
    dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    sorted_dates = sort_dates_chronologically(dates)
    print(sorted_dates)