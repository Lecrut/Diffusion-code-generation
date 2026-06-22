class DateSorter:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def _parse_date(date_str):
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        return (year, month, day)

    @classmethod
    def sort_dates(cls, date_list):
        return sorted(date_list, key=lambda d: cls._parse_date(d))

if __name__ == '__main__':
    unsorted_dates = ['2024-12-31', '2020-02-29', '2023-01-01', '2021-07-15']
    sorted_dates = DateSorter.sort_dates(unsorted_dates)
    print(sorted_dates)