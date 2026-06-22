def compare_dates(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_dates = sorted(set1.intersection(set2), reverse=True)
    return common_dates

if __name__ == '__main__':
    dates_list1 = ["2023-04-01", "2023-05-15", "2023-06-20"]
    dates_list2 = ["2023-05-15", "2023-07-25", "2023-04-01"]
    result = compare_dates(dates_list1, dates_list2)
    print(result)