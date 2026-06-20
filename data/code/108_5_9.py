from datetime import datetime

class DateUtil:
    @staticmethod
    def get_day_of_month(date: datetime) -> int:
        return date.day

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15)
    util_instance = DateUtil()
    day_of_month = util_instance.get_day_of_month(sample_date)
    print(day_of_month)