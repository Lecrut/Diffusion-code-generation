import datetime

class DateDifference:
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    @staticmethod
    def parse_date(date_str):
        return datetime.datetime.strptime(date_str, DateDifference.DATE_FORMAT)

    @staticmethod
    def get_difference_minutes(date1, date2):
        difference = abs(date2 - date1)
        return int(difference.total_seconds() / 60)

if __name__ == '__main__':
    date_a_str = "2023-10-29 10:00:00"
    date_b_str = "2023-11-02 14:30:00"
    
    date_a = DateDifference.parse_date(date_a_str)
    date_b = DateDifference.parse_date(date_b_str)
    
    difference_minutes = DateDifference.get_difference_minutes(date_a, date_b)
    print(difference_minutes)