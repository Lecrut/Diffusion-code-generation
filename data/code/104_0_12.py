from datetime import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def is_earlier(date_str1: str, date_str2: str) -> bool:
        date1 = datetime.strptime(date_str1, DateComparator.DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DateComparator.DATE_FORMAT)
        return date1 < date2

if __name__ == '__main__':
    sample_date1 = "2023-10-05"
    sample_date2 = "2023-10-15"
    print(DateComparator.is_earlier(sample_date1, sample_date2))