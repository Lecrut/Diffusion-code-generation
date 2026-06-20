class DateSorter:
    def sort_dates(self, date_list):
        return sorted(date_list, key=lambda x: (x[0], x[1], x[2]))

if __name__ == '__main__':
    sorter = DateSorter()
    sample_dates = [(2023, 4, 5), (2022, 1, 1), (2023, 1, 15)]
    sorted_dates = sorter.sort_dates(sample_dates)
    print(sorted_dates)