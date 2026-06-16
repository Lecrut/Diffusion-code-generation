import datetime
def sort_dates(date_strings):
    return sorted(date_strings, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
if __name__ == '__main__':
    unsorted_dates = ["2023-10-26", "2023-10-25", "2023-10-27", "2023-10-24"]
    sorted_dates = sort_dates(unsorted_dates)
    print(sorted_dates)