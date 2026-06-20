from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

def sort_dates(date_list):
    parsed_dates = [parse_date(date) for date in date_list]
    sorted_dates = sorted(parsed_dates)
    return [date.strftime('%Y-%m-%d') for date in sorted_dates]

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2022-12-31', '2023-04-01']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)