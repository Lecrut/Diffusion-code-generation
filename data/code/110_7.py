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
        '2023-10-01',
        '31-12-2023',
        '01/01/2024'
    ]
    sorted_dates = sort_inconsistent_dates(sample_dates)
    print(sorted_dates)