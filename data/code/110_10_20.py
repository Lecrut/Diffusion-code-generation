from datetime import datetime

class DateSorter:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def _parse(date_str):
        return datetime.strptime(date_str, DateSorter.DATE_FORMAT)

    @staticmethod
    def sort_dates(date_strings):
        return sorted(date_strings, key=DateSorter._parse)

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    result = DateSorter.sort_dates(sample_dates)
    print(result)