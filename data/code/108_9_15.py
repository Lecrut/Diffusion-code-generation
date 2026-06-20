import datetime

class DateUtils:
    @staticmethod
    def get_day_of_month(date_instance: datetime.datetime) -> int:
        return date_instance.day

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 27)
    day = DateUtils.get_day_of_month(sample_date)
    print(f"Day of the month for {sample_date}: {day}")