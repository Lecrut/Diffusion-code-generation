from datetime import datetime

def compare_date_lists(list1, list2):
    try:
        date_format = '%Y-%m-%d'
        list1_dates = set((datetime.strptime(date, date_format) for date in list1))
        list2_dates = set((datetime.strptime(date, date_format) for date in list2))
        common_dates = sorted(list(list1_dates & list2_dates), reverse=True)
        return [date.strftime(date_format) for date in common_dates]
    except ValueError as e:
        raise ValueError('Invalid date format in the input lists.') from e
if __name__ == '__main__':
    dates_list1 = ['2023-04-01', '2023-05-01', '2023-06-01']
    dates_list2 = ['2023-05-01', '2023-07-01', '2023-08-01']
    result = compare_date_lists(dates_list1, dates_list2)
    print(result)