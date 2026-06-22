from datetime import datetime

class DateSorter:
    FORMAT_STRING = '%Y-%m-%d'

    @staticmethod
    def _convert_to_datetime(date_str):
        return datetime.strptime(date_str, DateSorter.FORMAT_STRING)

    def sort(self, dates):
        return sorted(dates, key=self._convert_to_datetime)

if __name__ == '__main__':
    unsorted_dates = ['2024-02-29', '2023-01-15', '2023-01-15', '2025-12-31', '2022-07-04']
    sorter = DateSorter()
    result = sorter.sort(unsorted_dates)
    print(result)