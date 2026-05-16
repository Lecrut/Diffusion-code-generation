import datetime
def sort_inconsistent_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        formats_to_try = [
            '%m/%d/%Y',
            '%Y-%m-%d',
            '%m-%d-%Y',
            '%d/%m/%Y',
            '%d-%m-%Y',
            '%Y/%m/%d'
        ]
        parsed = None
        for fmt in formats_to_try:
            try:
                parsed = datetime.datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        if parsed:
            parsed_dates.append(parsed)
        else:
            raise ValueError(f"Could not parse date string: {date_str}")
    return sorted(parsed_dates)
if __name__ == '__main__':
    sample_dates = [
        '12/31/2023',
        '2024-01-15',
        '05/20/2022',
        '2023/11/01',
        '10-25-2024',
        '01/01/2024'
    ]
    try:
        sorted_dates = sort_inconsistent_dates(sample_dates)
        for date in sorted_dates:
            print(date.strftime('%Y-%m-%d'))
    except ValueError as e:
        print(f"Error: {e}")