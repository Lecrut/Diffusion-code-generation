class DateSorter:
    def sort(self, date_list):
        if not all(isinstance(d, tuple) and len(d) == 3 and all(isinstance(i, int) for i in d) for d in date_list):
            raise ValueError("All elements must be tuples of three integers.")
        return sorted(date_list, key=lambda x: (x[0], x[1], x[2]))

if __name__ == '__main__':
    sorter = DateSorter()
    sample_dates = [(2023, 4, 5), (2022, 1, 1), (2023, 1, 15)]
    sorted_dates = sorter.sort(sample_dates)
    print(sorted_dates)