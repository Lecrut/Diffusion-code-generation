import datetime

class DateUtils:
    @staticmethod
    def get_day_of_month(date_instance: datetime.date) -> int:
        return date_instance.day

if __name__ == '__main__':
    sample_date_1 = datetime.date(2023, 10, 27)
    result_1 = DateUtils.get_day_of_month(sample_date_1)
    print(f"Day of the month for {sample_date_1}: {result_1}")
    
    sample_date_2 = datetime.date(1999, 1, 1)
    result_2 = DateUtils.get_day_of_month(sample_date_2)
    print(f"Day of the month for {sample_date_2}: {result_2}")
    
    sample_date_3 = datetime.date(2024, 2, 29)
    result_3 = DateUtils.get_day_of_month(sample_date_3)
    print(f"Day of the month for {sample_date_3}: {result_3}")