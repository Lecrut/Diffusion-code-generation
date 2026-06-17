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
            parsed_dates.append((False, float('inf'), date_str))
        else:
            parsed_dates.append((True, parsed_date.timestamp(), date_str))
    sorted_dates = sorted(parsed_dates, key=lambda x: x[1])
    result = [item[2] for item in sorted_dates]
    return result
if __name__ == '__main__':
    sample_dates = [
        '03/15/2023',                  
        '2024-01-01',                  
        '12/31/2022',                  
        '2023-05-20',                  
        '01-02-2024',                                                                                  
        '2022-11-11'                   
    ]
    sorted_list = flexible_date_sort(sample_dates)
    print(sorted_list)