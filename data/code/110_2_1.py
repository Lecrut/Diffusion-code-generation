class DateSorter:
    def sort_dates(self, date_list):
        return sorted(date_list)
if __name__ == '__main__':
    sorter = DateSorter()
    sample_dates = ["2023-01-15", "2022-12-31", "2023-01-01", "2022-11-20"]
    sorted_dates = sorter.sort_dates(sample_dates)
    print(sorted_dates)