import datetime

def sort_date_strings(date_list):
    try:
        date_objects = [datetime.datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_list]
        sorted_date_objects = sorted(date_objects)
        return [sorted_date_objects[i].strftime('%Y-%m-%d') for i in range(len(sorted_date_objects))]
    except ValueError as e:
        raise ValueError("Invalid date format in input list") from e

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2022-12-31', '2023-04-01']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)