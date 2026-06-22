from datetime import datetime

def compare_dates(list1, list2):
    date_format = "%Y-%m-%d"
    set1 = {datetime.strptime(date, date_format) for date in list1}
    set2 = {datetime.strptime(date, date_format) for date in list2}
    common_dates = sorted(set1 & set2, reverse=True)
    return [date.strftime(date_format) for date in common_dates]

if __name__ == '__main__':
    dates_list1 = ["2023-04-01", "2023-05-15", "2023-06-20"]
    dates_list2 = ["2023-05-15", "2023-07-01", "2023-08-10"]
    result = compare_dates(dates_list1, dates_list2)
    print(result)