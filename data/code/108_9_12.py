import datetime

class DateExtractor:
    @staticmethod
    def get_day_of_month(date_instance: datetime.datetime) -> int:
        return date_instance.day

if __name__ == '__main__':
    sample_date_1 = datetime.datetime(2023, 10, 27)
    result_1 = DateExtractor.get_day_of_month(sample_date_1)
    print(f"Day of the month for {sample_date_1}: {result_1}")
    
    sample_date_2 = datetime.datetime(1999, 1, 1)
    result_2 = DateExtractor.get_day_of_month(sample_date_2)
    print(f"Day of the month for {sample_date_2}: {result_2}")
    
    sample_date_3 = datetime.datetime(2024, 2, 29)
    result_3 = DateExtractor.get_day_of_month(sample_date_3)
    print(f"Day of the month for {sample_date_3}: {result_3}")