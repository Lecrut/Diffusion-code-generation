from datetime import datetime

class DateUtil:
    @staticmethod
    def is_weekend(date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.weekday() >= 5

if __name__ == '__main__':
    util = DateUtil()
    print(util.is_weekend('2023-10-07'))
    print(util.is_weekend('2023-10-08'))
    print(util.is_weekend('2023-10-09'))