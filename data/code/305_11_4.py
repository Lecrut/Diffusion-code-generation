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
        "2023-10-25",
        "2023-10-27",
        "2023-10-24",
        "2023-10-25"
    ]
    sorted_list = sort_dates(sample_dates)
    print(sorted_list)