import datetime
class DateSorter:
    def sort_dates(self, date_list):
        return sorted(date_list)
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 26)
    date2 = datetime.date(2023, 1, 15)
    date3 = datetime.date(2023, 5, 1)
    date4 = datetime.date(2022, 12, 31)
    unsorted_dates = [date1, date2, date3, date4]
    sorter = DateSorter()
    sorted_dates = sorter.sort_dates(unsorted_dates)
    print(sorted_dates)