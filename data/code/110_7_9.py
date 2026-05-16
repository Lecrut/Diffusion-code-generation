import datetime
def sort_inconsistent_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        formats_to_try = [
            '%m/%d/%Y',
            '%Y-%m-%d',
            '%m-%d-%Y',
            '%d/%m/%Y',
            '%d-%m-%Y'
        ]
        parsed = None
        for fmt in formats_to_try:
            try:
                parsed = datetime.datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        if parsed is not None:
            parsed_dates.append(parsed)
        else:
            raise ValueError(f"Could not parse date string: {date_str}")
    parsed_dates.sort()
    return [d.strftime('%Y-%m-%d') for d in parsed_dates]
if __name__ == '__main__':
    sample_dates = [
        '12/31/2023',
        '2024-01-15',
        '05/20/2022',
        '2023-11-01',
        '01/01/2024',
        '2022-05-10'
    ]
    try:
        sorted_dates = sort_inconsistent_dates(sample_dates)
        print(sorted_dates)
    except ValueError as e:
        print(f"Error: {e}")