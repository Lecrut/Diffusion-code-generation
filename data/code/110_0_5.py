class DateSorter:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def sort_dates(date_list):
        return sorted(date_list, key=lambda date: (int(date[:4]), int(date[5:7]), int(date[8:])))

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-01-15', '2023-03-20']
    sorter = DateSorter()
    sorted_dates = sorter.sort_dates(sample_dates)
    print(sorted_dates)