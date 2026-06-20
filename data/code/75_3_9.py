from datetime import datetime

class DateUtils:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def calculate_difference(date_str1, date_str2):
        date1 = datetime.strptime(date_str1, DateUtils.DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DateUtils.DATE_FORMAT)
        return abs(date2 - date1)

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2022-12-31"
    difference = DateUtils.calculate_difference(date1, date2)
    print(difference)