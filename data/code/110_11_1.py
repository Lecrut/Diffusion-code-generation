import datetime
def sort_dates(date_strings):
    date_objects = [datetime.datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_strings]
    sorted_date_objects = sorted(date_objects)
    sorted_date_strings = [dt.strftime('%Y-%m-%d') for dt in sorted_date_objects]
    return sorted_date_strings
if __name__ == '__main__':
    sample_dates = ["2023-10-26", "2023-10-25", "2023-10-27", "2023-10-24"]
    sorted_result = sort_dates(sample_dates)
    print(sorted_result)