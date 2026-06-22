def compare_dates(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_dates = sorted(set1 & set2, reverse=True)
    return common_dates

if __name__ == '__main__':
    dates_list1 = ["2023-04-01", "2023-03-15", "2023-02-28"]
    dates_list2 = ["2023-03-15", "2023-02-28", "2023-01-31"]
    print(compare_dates(dates_list1, dates_list2))