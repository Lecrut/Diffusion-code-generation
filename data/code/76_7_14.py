from datetime import datetime

class DateUtils:
    @staticmethod
    def days_between(date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        time_difference = abs(date2 - date1)
        return time_difference.days

if __name__ == '__main__':
    sample_date_a = "2023-04-15"
    sample_date_b = "2023-08-30"
    days = DateUtils.days_between(sample_date_a, sample_date_b)
    print(days)