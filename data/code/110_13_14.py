import datetime

class DateSorter:

    @staticmethod
    def from_iso(date_string):
        return datetime.datetime.fromisoformat(date_string)

    @classmethod
    def sort_dates(cls, date_strings):
        return sorted(date_strings, key=cls.from_iso)
if __name__ == '__main__':
    sample_dates = ['2023-01-01T12:00:00Z', '2022-12-31T23:59:59Z', '2023-01-02T00:00:00Z']
    sorter = DateSorter()
    sorted_dates = sorter.sort_dates(sample_dates)
    print(sorted_dates)