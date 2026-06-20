import datetime

class DateUtil:
    DAY_OF_WEEK_MONDAY = 0

    @staticmethod
    def day_of_week(date_str):
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return (date_obj.weekday() + 1) % 7

if __name__ == '__main__':
    sample_date = "2023-04-15"
    print(DateUtil.day_of_week(sample_date))