from datetime import date
class DateSorter:
    def sort_dates(self, date_list):
        return sorted(date_list)
if __name__ == '__main__':
    unsorted_dates = [
        date(2023, 10, 26),
        date(2023, 1, 1),
        date(2024, 5, 15),
        date(2023, 10, 25)
    ]
    sorter = DateSorter()
    sorted_dates = sorter.sort_dates(unsorted_dates)
    for d in sorted_dates:
        print(d)