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
def sort_date_strings(date_list):
    parsed_dates = []
    for date_str in date_list:
        dt_obj = parse_date_string(date_str)
        if dt_obj:
            parsed_dates.append(dt_obj)
        else:
            pass
    sortable_list = []
    for date_str in date_list:
        dt_obj = parse_date_string(date_str)
        if dt_obj:
            sortable_list.append((dt_obj, date_str))
    sortable_list.sort(key=lambda x: x[0])
    sorted_dates = [item[1] for item in sortable_list]
    return sorted_dates
if __name__ == '__main__':
    sample_dates = [
        '12/31/2023',
        '2024-01-15',
        '05/20/2022',
        '2023-11-01',
        '01/01/2024',
        '31/12/2022',
        'invalid-date'
    ]
    sorted_result = sort_date_strings(sample_dates)
    print(sorted_result)