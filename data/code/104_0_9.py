from datetime import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        return datetime.strptime(date_str, DateComparator.DATE_FORMAT)

    @staticmethod
    def is_earlier(date1: datetime, date2: datetime) -> bool:
        return date1 < date2

if __name__ == '__main__':
    sample_date_str1 = "2023-10-26"
    sample_date_str2 = "2023-11-15"
    
    date1 = DateComparator.parse_date(sample_date_str1)
    date2 = DateComparator.parse_date(sample_date_str2)
    
    result = DateComparator.is_earlier(date1, date2)
    print(result)