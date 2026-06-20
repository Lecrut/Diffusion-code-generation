import datetime

def sort_date_strings(date_list):
    date_objects = []
    for date_str in date_list:
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            date_objects.append((date_obj, date_str))
        except ValueError:
            continue
    sorted_date_objects = sorted(date_objects)
    return [date_str for _, date_str in sorted_date_objects]

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2022-12-31', '2023-04-01']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)