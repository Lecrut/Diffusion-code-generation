class DateSorter:
    @staticmethod
    def sort_date_tuples(date_list):
        return sorted(date_list, key=lambda x: (x[0], x[1], x[2]))

if __name__ == '__main__':
    sample_dates = [(2023, 4, 5), (2022, 1, 1), (2023, 1, 15)]
    sorter = DateSorter()
    sorted_dates = sorter.sort_date_tuples(sample_dates)
    print(sorted_dates)