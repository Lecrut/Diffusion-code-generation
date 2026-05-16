from datetime import datetime
def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            parsed_dates.append(date_obj)
        except ValueError:
            pass
    parsed_dates.sort()
    sorted_date_strings = [date.strftime('%Y-%m-%d') for date in parsed_dates]
    return sorted_date_strings
if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2023-01-01",
        "2024-05-15",
        "invalid-date",
        "2023-12-31"
    ]
    sorted_list = sort_dates(sample_dates)
    print(sorted_list)