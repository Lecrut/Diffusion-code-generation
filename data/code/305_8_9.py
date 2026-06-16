from datetime import datetime
def flexible_date_sort(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        parsed_date = None
        formats_to_try = [
            '%m/%d/%Y',              
            '%Y-%m-%d',              
            '%m-%d-%Y',                                              
            '%d.%m.%Y'               
        ]
        for fmt in formats_to_try:
            try:
                parsed_date = datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        if parsed_date:
            parsed_dates.append((parsed_date, date_str))
        else:
            parsed_dates.append((None, date_str))
    parsed_dates.sort(key=lambda x: x[0])
    sorted_dates = [date_str for _, date_str in parsed_dates]
    return sorted_dates
if __name__ == '__main__':
    sample_dates = [
        '12/31/2023',
        '2024-01-15',
        '05/20/2022',
        '2023-11-01',
        '01/01/2024',
        '2022-12-31'
    ]
    sorted_list = flexible_date_sort(sample_dates)
    print(sorted_list)