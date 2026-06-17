import datetime
def flexible_date_sort(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        formats_to_try = [
            '%m/%d/%Y',
            '%Y-%m-%d'
        ]
        parsed = None
        for fmt in formats_to_try:
            try:
                if '/' in date_str:
                    dt_obj = datetime.datetime.strptime(date_str, fmt)
                else:
                    dt_obj = datetime.datetime.strptime(date_str, fmt)
                parsed = dt_obj
                break
            except ValueError:
                continue
        if parsed is not None:
            parsed_dates.append((parsed, date_str))
        else:
            parsed_dates.append((None, date_str))
    sorted_dates = sorted(parsed_dates, key=lambda x: x[0])
    return [item[1] for item in sorted_dates]
if __name__ == '__main__':
    sample_dates = [
        '12/31/2023',
        '2024-01-15',
        '03/01/2023',
        '2023-11-20',
        '05/10/2024',
        '2022-07-01'
    ]
    sorted_list = flexible_date_sort(sample_dates)
    print(sorted_list)