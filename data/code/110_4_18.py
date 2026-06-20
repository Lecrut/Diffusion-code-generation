class DateSorter:
    def sort_dates(self, date_list):
        return sorted(date_list)

if __name__ == '__main__':
    sorter = DateSorter()
    sample_dates = [(2023, 1, 15), (2022, 12, 25), (2024, 1, 1)]
    sorted_dates = sorter.sort_dates(sample_dates)
    print("Sorted Dates:")
    for date in sorted_dates:
        print(f"{date[0]}-{date[1]:02d}-{date[2]:02d}")