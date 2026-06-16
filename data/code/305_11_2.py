import datetime
def sort_dates(date_strings):
    date_objects = []
    for date_str in date_strings:
        try:
            date_objects.append(datetime.datetime.strptime(date_str, '%Y-%m-%d').date())
        except ValueError:
            pass
    date_objects.sort()
    return [d.strftime('%Y-%m-%d') for d in date_objects]
if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2024-01-15",
        "2023-12-31",
        "2024-01-01",
        "2023-10-26"
    ]
    sorted_list = sort_dates(sample_dates)
    print(sorted_list)