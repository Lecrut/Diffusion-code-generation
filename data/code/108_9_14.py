import datetime

def get_day_of_month(date_instance):
    if not isinstance(date_instance, datetime.datetime):
        raise ValueError("Input must be an instance of datetime.datetime")
    return date_instance.day

if __name__ == '__main__':
    sample_date_1 = datetime.datetime(2023, 10, 27)
    print(f"Day of the month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    sample_date_2 = datetime.datetime(1999, 1, 1)
    print(f"Day of the month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    sample_date_3 = datetime.datetime(2024, 2, 29)
    print(f"Day of the month for {sample_date_3}: {get_day_of_month(sample_date_3)}")