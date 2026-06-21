class DateSorter:
    DATE_FORMAT = '%Y-%m-%d'
    
    @staticmethod
    def _parse_date(date_string):
        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
        return (year, month, day)

    def sort_dates(self, dates):
        return sorted(dates, key=lambda d: self._parse_date(d))

if __name__ == '__main__':
    dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01', '2020-02-29']
    sorter = DateSorter()
    result = sorter.sort_dates(dates)
    print(result)