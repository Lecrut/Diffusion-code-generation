import datetime
def sort_dates(date_strings):
    date_objects = []
    for date_str in date_strings:
        try:
            date_objects.append(datetime.datetime.strptime(date_str, '%Y-%m-%d'))
        except ValueError:
            pass
    date_objects.sort()
    sorted_date_strings = [dt.strftime('%Y-%m-%d') for dt in date_objects]
    return sorted_date_strings
if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2024-01-15",
        "2023-12-31",
        "2024-01-01",
        "2023-10-26"
    ]
    sorted_result = sort_dates(sample_dates)
    print(sorted_result)