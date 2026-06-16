from datetime import datetime
def flexible_date_sort(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        parsed_date = None
        formats_to_try = [
            '%m/%d/%Y',              
            '%Y-%m-%d',              
            '%m-%d-%Y',                                              
        ]
        for fmt in formats_to_try:
            try:
                parsed_date = datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        if parsed_date is None:
            parsed_date = datetime(9999, 12, 31)
        if parsed_date:
            parsed_dates.append((parsed_date, date_str))
        else:
            parsed_dates.append((datetime(9999, 12, 31), date_str))
    parsed_dates.sort(key=lambda x: x[0])
    return [item[1] for item in parsed_dates]
if __name__ == '__main__':
    sample_dates = [
        '12/31/2023',
        '2024-01-15',
        '03/01/2024',
        '2023-10-20',
        '05/10/2024',
        '2024-02-29',                  
        '11/11/2023'
    ]
    sorted_dates = flexible_date_sort(sample_dates)
    print(sorted_dates)