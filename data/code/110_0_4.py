class DateSorter:
    DATE_PATTERN = '%Y-%m-%d'

    @staticmethod
    def parse_date(date_str):
        from datetime import datetime
        return datetime.strptime(date_str, DateSorter.DATE_PATTERN).date()

    @staticmethod
    def sort_chronologically(dates):
        return sorted(dates, key=DateSorter.parse_date)

if __name__ == '__main__':
    input_dates = ['2023-01-15', '2020-02-29', '2023-12-31', '2021-05-10']
    sorted_dates = DateSorter.sort_chronologically(input_dates)
    print(sorted_dates)