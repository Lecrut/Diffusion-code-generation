from datetime import datetime

class DateUtils:
    @staticmethod
    def calculate_days_between(date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        time_difference = abs(date2 - date1)
        return time_difference.days

if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-05-20"
    days = DateUtils.calculate_days_between(date_a, date_b)
    print(days)