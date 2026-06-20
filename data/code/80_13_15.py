import datetime

class DateComparator:
    DATE_FORMAT = '%Y-%m-%d'
    
    @staticmethod
    def parse_date(date_str: str) -> datetime.date:
        return datetime.datetime.strptime(date_str, DateComparator.DATE_FORMAT).date()
    
    @staticmethod
    def compare_dates(date_str1: str, date_str2: str) -> int:
        date1 = DateComparator.parse_date(date_str1)
        date2 = DateComparator.parse_date(date_str2)
        if date1 < date2:
            return -1
        elif date1 > date2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    sample_date_1 = '2023-04-01'
    sample_date_2 = '2023-04-02'
    result = DateComparator.compare_dates(sample_date_1, sample_date_2)
    print(result)