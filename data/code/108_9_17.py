from datetime import datetime

def get_day_of_month(date_instance: datetime) -> int:
    if not isinstance(date_instance, datetime):
        raise ValueError("Input must be an instance of datetime")
    return date_instance.day

if __name__ == '__main__':
    sample_date_1 = datetime(2023, 10, 27)
    result_1 = get_day_of_month(sample_date_1)
    print(f"Day of the month for {sample_date_1}: {result_1}")
    
    sample_date_2 = datetime(1999, 1, 1)
    result_2 = get_day_of_month(sample_date_2)
    print(f"Day of the month for {sample_date_2}: {result_2}")
    
    sample_date_3 = datetime(2024, 2, 29)
    result_3 = get_day_of_month(sample_date_3)
    print(f"Day of the month for {sample_date_3}: {result_3}")