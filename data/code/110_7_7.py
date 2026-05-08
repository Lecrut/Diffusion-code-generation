import datetime
def parse_date_string(date_str):
    formats = [
        '%m/%d/%Y',
        '%Y-%m-%d',
        '%m-%d-%Y',
        '%d/%m/%Y',
        '%d-%m-%Y'
    ]
    for fmt in formats:
        try:
            dt_obj = datetime.datetime.strptime(date_str, fmt)
            return dt_obj
        except ValueError:
            continue
    return None
def sort_inconsistent_dates(date_list):
    parsed_dates = []
    for date_str in date_list:
        dt_obj = parse_date_string(date_str)
        if dt_obj:
            parsed_dates.append(dt_obj)
        else:
            print(f"Warning: Could not parse date string: {date_str}")
    if not parsed_dates:
        return []
    parsed_dates.sort()
    return [d.strftime('%Y-%m-%d') for d in parsed_dates]
if __name__ == '__main__':
    sample_dates = [
        '12/31/2023',
        '2024-01-15',
        '05/20/2022',
        '2023-11-01',
        '10-10-2023',
        '2022-05-20'
    ]
    sorted_dates = sort_inconsistent_dates(sample_dates)
    print(sorted_dates)