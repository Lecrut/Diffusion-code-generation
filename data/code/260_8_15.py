from datetime import datetime

def compare_dates(list1, list2):
    set1 = set(map(datetime.strptime, list1, ['%Y-%m-%d']))
    set2 = set(map(datetime.strptime, list2, ['%Y-%m-%d']))
    common_dates = sorted(set1 & set2, reverse=True)
    return [date.strftime('%Y-%m-%d') for date in common_dates]

if __name__ == '__main__':
    dates_list1 = ['2023-04-01', '2023-05-01', '2023-06-01']
    dates_list2 = ['2023-05-01', '2023-07-01', '2023-04-01']
    result = compare_dates(dates_list1, dates_list2)
    print(result)